import datetime

import pydantic


class IncomingOrder(pydantic.BaseModel):
    email: str | None = None
    phone: str | None = None
    tickets_count: int
    qr_alias: str

    @pydantic.validator('email', 'phone')
    def validate_email_or_phone(cls, v, values, **kwargs):
        if not v:
            raise ValueError('email or phone must be set')
        return v


class Payment(pydantic.BaseModel):
    amount: int
    order: str
    merchant_id: str


class EventInfoResponsePayload(pydantic.BaseModel):
    name: str
    organization_name: str
    description: str
    date: datetime.datetime
    price: str
    logo: str
    background: str


class RaifQRCodeRequest(pydantic.BaseModel):
    qrType: str
    amount: int
    currency: str | None = None
    order: str
    sbpMerchantId: str
    redirectUrl: str


class SBPQRCode(pydantic.BaseModel):
    qrId: str
    qrStatus: str
    qrUrl: str
