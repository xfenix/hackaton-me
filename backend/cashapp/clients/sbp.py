import httpx
from django.conf import settings

from cashapp import pydantic_models


class RaifSBPClient:
    @staticmethod
    async def send_payment(payment: pydantic_models.Payment) -> pydantic_models.SBPQRCode | None:
        redirect_url: str = f'{settings.APP_URL_BASE}/{payment.order}'
        qr_code_request: pydantic_models.RaifQRCodeRequestPayload = pydantic_models.RaifQRCodeRequestPayload(
            qrType=settings.QR_TYPE,
            amount=payment.amount,
            currency=settings.CURRENCY,
            order=payment.order,
            sbpMerchantId=payment.merchant_id,
            redirectUrl=redirect_url,
        )

        async with httpx.AsyncClient() as client:
            try:
                result: httpx.Response = await client.post(settings.QR_GENERATION_URL, json=qr_code_request.dict())
                result.raise_for_status()
            except httpx.HTTPError as exc:
                print(f"Error while requesting {exc} {result.content}.")
                return None

            return pydantic_models.SBPQRCode(**result.json())
