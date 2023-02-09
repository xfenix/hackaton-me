import httpx
from django.conf import settings

from cashapp import pydantic_models


class RaifSBPClient:
    @staticmethod
    async def send_payment(self, payment: pydantic_models.Payment) -> None:
        redirect_url: str = f'{settings.URL_BASE}/{payment.order}'
        qr_code_request: pydantic_models.RaifQRCodeRequestPayload = pydantic_models.RaifQRCodeRequestPayload(
            qrType=settings.QR_TYPE,
            amount=payment.amount,
            currency=settings.CURRENCY,
            order=payment.order,
            sbpMerchantId=payment.merchant_id,
            redirectUrl=redirect_url,
        )

        async with httpx.AsyncClient() as client:
            result: httpx.Response = await client.post(settings.QR_GENERATION_URL, qr_code_request.json())
            return pydantic_models.SBPQRCode(**result.json())
