from django.http import HttpResponse
from django.views.generic import View
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, JsonResponse
from django.utils.decorators import classonlymethod, method_decorator
from django.views.decorators.csrf import csrf_exempt
from cashapp import models
import asyncio
from cashapp import pydantic_models
from cashapp.services import barcodes


@method_decorator(csrf_exempt, name='dispatch')
class MakeOrderView(View):

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def post(self, request) -> JsonResponse | HttpResponseNotFound | HttpResponseBadRequest | HttpResponseServerError:
        order_income: pydantic_models.OrderIncomeModel = pydantic_models.OrderIncomeModel(**request.POST)

        event: models.Event | None = models.EventQRCode.objects.filter(alias=order_income.event_alias).first()
        if not event:
            raise HttpResponseNotFound('Event not found')

        new_order: models.Order = models.Order.objects.create(
            email=order_income.email,
            phone=order_income.phone,
            tickets_count=order_income.tickets_count,
            event=event.id
        )
        new_order.save(returning=True)
        return HttpResponse('Order was made')


@method_decorator(csrf_exempt, name='dispatch')
class MakeQr(View):

    def get(self, request: HttpRequest, alias: str) -> HttpResponse | HttpResponseNotFound:

        event: models.EventQRCode | None = models.EventQRCode.objects.filter(alias=alias).first()
        if not event:
            return HttpResponseNotFound('Event not found')

        new_qr: str = barcodes.qr_instance.generate(alias)
        return HttpResponse(new_qr, headers={'Content-Type': 'image/svg+xml'})
