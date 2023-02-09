import asyncio

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
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


@method_decorator(csrf_exempt, name='dispatch')
class MakeOrderView(ViewBase):
    async def post(
        self, request
    ) -> JsonResponse | HttpResponseNotFound | HttpResponseBadRequest | HttpResponseServerError:
        incoming_order: pydantic_models.IncomingOrder = pydantic_models.IncomingOrder(**request.POST)

        event_qr_code: models.EventQRCode | None = models.EventQRCode.objects.filter(
            alias=incoming_order.qr_alias
        ).first()
        if not event_qr_code:
            raise HttpResponseNotFound('Event not found')

        new_order: models.Order = models.Order.objects.create(
            email=incoming_order.email,
            phone=incoming_order.phone,
            tickets_count=incoming_order.tickets_count,
            event=event_qr_code.event,
        )
        new_order.save()

        payment: pydantic_models.Payment = pydantic_models.Payment(
            amount=order.tickets_count * event_qr_code.price,
            order=event_qr_code.uuid,
            merchant_id=event_qr_code.event.organization.merchant_id,
        )

        payment_qr_code: pydantic_models.SBPQRCode = await sbp.RaifSBPClient.send_payment(payment)

        order: models.Order = models.Order.objects.filter(id=new_order.id).update(
            qr_id=payment_qr_code.qrId, qr_status=payment_qr_code.qrStatus, qr_url=payment_qr_url.qrUrl
        )

        return redirect(new_sbp_qr_code.qr_url)


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
        event_info: pydantic_models.EventInfoResponseModel = pydantic_models.EventInfoResponseModel(
            name=event.name,
            organization_name=event_organization.name,
            description=event.description,
            date=event.event_date,
            price=event_qr_code.price,
            logo=event.logo,
            background=event.background,
        )
        return JsonResponse(event_info.dict())
