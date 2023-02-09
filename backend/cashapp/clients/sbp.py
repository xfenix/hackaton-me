from cashapp import models, pydantic_models

import httpx


class RaifSBPClient:
    @staticethod
    async def send_payment(self, payment: Payment) -> None:
        redirect_url: str = f'{settings.REDIRECT_URL_BASE}/{payment.order}'
        qr_code_request: pydantic_models.RaifQRCodeRequest = pydantic_models.RaifQRCodeRequest(
            qrType=settings.qrType,
            amount=payment.amount,
            currency=settings.CURRENCY,
            order=payment.order,
            sbpMerchantId=payment.merchant_id,
            redirectUrl=redirect_url,
        )

        sbp_qr_code: SBPQRCode
        async with httpx.AsyncClient() as client:
            result: httpx.Response = await client.get(settings.QR_GENERATION_URL, qr_code_request.json())
            sbp_qr_code = SBPQRCode(**result.json())

        pass
