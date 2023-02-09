import httpx
from django.conf import settings

from cashapp import models, pydantic_models


class RaifSBPClient:
    @staticmethod
    async def send_payment(self, payment: Payment) -> None:
        redirect_url: str = f'{settings.URL_BASE}/{payment.order}'
        qr_code_request: pydantic_models.RaifQRCodeRequest = pydantic_models.RaifQRCodeRequest(
            qrType=settings.qrType,
            amount=payment.amount,
            currency=settings.CURRENCY,
            order=payment.order,
            sbpMerchantId=payment.merchant_id,
            redirectUrl=redirect_url,
        )

        async with httpx.AsyncClient() as client:
            result: httpx.Response = await client.post(settings.QR_GENERATION_URL, qr_code_request.json())
            return SBPQRCode(**result.json())
