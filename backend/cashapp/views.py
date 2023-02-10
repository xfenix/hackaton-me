import asyncio
import json

import pydantic
from asgiref.sync import sync_to_async
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseRedirect,
    HttpResponseServerError,
    JsonResponse,
)
from django.shortcuts import redirect
from django.utils.decorators import classonlymethod, method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from cashapp import models, pydantic_models
from cashapp.clients import sbp
from cashapp.services import barcodes


class ViewBase(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view


@sync_to_async
def create_new_order(incoming_order: pydantic_models.IncomingOrder, event_qr_code: models.EventQRCode) -> models.Order:
    new_order: models.Order = models.Order.objects.create(
        email=incoming_order.email if incoming_order.email else '',
        phone=incoming_order.phone if incoming_order.email else '',
        tickets_count=incoming_order.ticket_count,
        event=event_qr_code.event,
    )
    new_order.save()
    return new_order


@sync_to_async
def create_payment_from_qr_code(new_order: models.Order, event_qr_code: models.EventQRCode) -> pydantic_models.Payment:
    return pydantic_models.Payment(
        amount=new_order.tickets_count * event_qr_code.price,
        order=str(new_order.uuid),
        merchant_id=event_qr_code.event.organization.merchant_id,
    )


@sync_to_async
def update_order_from_qr(new_order: models.Order, payment_qr_code: pydantic_models.SBPQRCode) -> models.Order:
    models.Order.objects.filter(id=new_order.id).update(qr_id=payment_qr_code.qrId, qr_url=payment_qr_code.payload)
    return models.Order.objects.filter(id=new_order.id).first()


@method_decorator(csrf_exempt, name='dispatch')
class MakeOrderView(ViewBase):
    async def post(self, request) -> HttpResponseNotFound | HttpResponseServerError | HttpResponseRedirect:
        try:
            decoded_json: dict[str, str | int] = json.loads(request.body.decode('utf-8'))
            incoming_order: pydantic_models.IncomingOrder = pydantic_models.IncomingOrder(**decoded_json)
        except pydantic.ValidationError:
            return HttpResponseBadRequest("Please specify a email or phone, ticket count & qr code alias")

        event_qr_code: models.EventQRCode | None = await models.EventQRCode.objects.filter(
            alias=incoming_order.qr_alias
        ).afirst()
        if not event_qr_code:
            return HttpResponseNotFound('Event not found')

        new_order: models.Order = await create_new_order(incoming_order, event_qr_code)

        payment_qr_code: pydantic_models.SBPQRCode | None = await sbp.RaifSBPClient.send_payment(
            await create_payment_from_qr_code(new_order, event_qr_code)
        )

        if not payment_qr_code:
            return HttpResponseServerError("Failed to connect to SBP")

        order: models.Order = await update_order_from_qr(new_order, payment_qr_code)

        return redirect(order.qr_url)


@method_decorator(csrf_exempt, name='dispatch')
class MakeQr(View):
    def get(self, request: HttpRequest, alias: str) -> HttpResponse | HttpResponseNotFound:
        event: models.EventQRCode | None = models.EventQRCode.objects.filter(alias=alias).first()
        if not event:
            return HttpResponseNotFound('Event not found')

        new_qr: str = barcodes.qr_instance.generate(alias)
        return HttpResponse(new_qr, headers={'Content-Type': 'image/svg+xml'})


@method_decorator(csrf_exempt, name='dispatch')
class FetchEventView(View):
    def get(
        self, request: HttpRequest, alias: str
    ) -> JsonResponse | HttpResponseNotFound | HttpResponseBadRequest | HttpResponseServerError:
        event_qr_code: models.EventQRCode | None = models.EventQRCode.objects.get(alias=alias)
        if not event_qr_code:
            raise HttpResponseNotFound('Event QR-code not found')
        event: models.Event = models.Event.objects.get(id=event_qr_code.event.id)
        event_organization: models.Organization = models.Organization.objects.get(id=event.organization.id)
        event_info: pydantic_models.EventInfoResponsePayload = pydantic_models.EventInfoResponsePayload(
            name=event.name,
            organization_name=event_organization.name,
            description=event.description,
            date=event.event_date,
            price=event_qr_code.price,
            logo=event.logo,
            background=event.background,
        )
        return JsonResponse(event_info.dict())


@method_decorator(csrf_exempt, name='dispatch')
class Pdf417CodeView(View):
    def get(self, request: HttpRequest, uuid: str) -> HttpResponse | HttpResponseNotFound | HttpResponseBadRequest:
        order: models.Order | None = models.Order.objects.all()
        if not order:
            return HttpResponseNotFound('Order not found')
        ticket_number: int = request.GET.get('ticket-number', 0)
        if not ticket_number:
            return HttpResponseBadRequest('Ticket number not specified')
        new_qr: str = barcodes.PDF417Code()(uuid, ticket_number)
        return HttpResponse(new_qr, headers={'Content-Type': 'image/svg+xml'})


@method_decorator(csrf_exempt, name='dispatch')
class RaifPaymentView(View):
    def post(
        self, request: HttpRequest
    ) -> JsonResponse | HttpResponseNotFound | HttpResponseBadRequest | HttpResponseServerError:
        try:
            decoded_json: dict[str, str | int] = json.loads(request.body.decode('utf-8'))
            payment_request: pydantic_models.RaifPaymentRequestPayload = pydantic_models.RaifPaymentRequestPayload(
                **decoded_json
            )
        except pydantic.ValidationError:
            return HttpResponseBadRequest("Raif payment system request data validation error")
        current_order = models.Order.objects.get(qr_id=payment_request.qrId)
        current_order.status = models.Order.STATUS_MAP[payment_request.paymentStatus]
        current_order.save()
        return HttpResponse(f"Order has been processed with status: {payment_request.paymentStatus}.")
