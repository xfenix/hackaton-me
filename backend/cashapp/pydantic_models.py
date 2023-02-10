import datetime

import pydantic


class IncomingOrder(pydantic.BaseModel):
    email: str | None = ''
    phone: str | None = ''
    ticket_count: int
    qr_alias: str

    @pydantic.validator('email')
    def validate_email_or_phone_present(cls, email, values, **kwargs):
        print(values)
        if email or 'phone' in values and values['phone'] != None:
            return email

        raise ValueError('Email or phone must be set')


class Payment(pydantic.BaseModel):
    amount: int
    order: str
    merchant_id: str

class RaifPaymentRequestPayload(pydantic.BaseModel):
    transactionId: int
    qrId: str
    sbpMerchantId: str
    merchantId: int
    amount: int
    currency: str
    transactionDate: datetime.datetime
    paymentStatus: str
    additionalInfo: str
    order: str
    createDate: datetime.datetime


class EventInfoResponsePayload(pydantic.BaseModel):
    name: str
    organization_name: str
    description: str
    date: datetime.datetime
    price: str
    logo: str
    background: str


class RaifQRCodeRequestPayload(pydantic.BaseModel):
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
