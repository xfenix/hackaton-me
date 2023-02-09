import asyncio

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseServerError,
    JsonResponse,
)
from django.utils.decorators import classonlymethod, method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from cashapp import models, pydantic_models
from cashapp.services import barcodes


@method_decorator(csrf_exempt, name='dispatch')
class MakeOrderView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def post(
        self, request: HttpRequest
    ) -> JsonResponse | HttpResponseNotFound | HttpResponseBadRequest | HttpResponseServerError:
        order_income: pydantic_models.OrderIncomeModel = pydantic_models.OrderIncomeModel(**request.POST)

        event: models.Event | None = models.EventQRCode.objects.filter(alias=order_income.event_alias).first()
        if not event:
            raise HttpResponseNotFound('Event not found')

        new_order: models.Order = models.Order.objects.create(
            email=order_income.email, phone=order_income.phone, tickets_count=order_income.tickets_count, event=event.id
        )
        new_order.save(returning=True)
        return HttpResponse('Order was made')


@method_decorator(csrf_exempt, name='dispatch')
class MakeQr(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(self, request: HttpRequest, event_id: str) -> JsonResponse | HttpResponseNotFound:
        event: models.Event | None = models.Event.objects.filter(id=event_id).first()
        if not event:
            raise HttpResponseNotFound('Event not found')

        new_qr: str = barcodes.qr_instance.generate(event_id)
        return JsonResponse({'qr_code': new_qr})


@method_decorator(csrf_exempt, name='dispatch')
class FetchEventView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(
        self, request: HttpRequest, event_qr_code_id: int
    ) -> JsonResponse | HttpResponseNotFound | HttpResponseBadRequest | HttpResponseServerError:
        event_qr_code: models.EventQRCode | None = models.EventQRCode.objects.get(id=event_qr_code_id)
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
        return JsonResponse(dict(event_info))
