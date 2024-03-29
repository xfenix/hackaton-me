import datetime
import re

import pydantic


RE_PHONE_CLEANUP: re.Pattern = re.compile(r'[^0-9]')
RE_EMAIL_VALIDTION: re.Pattern = re.compile(r'[^@]+@[^@]+\.[^@]+')


class IncomingOrder(pydantic.BaseModel):
    email: str | None = ''
    phone: str | None = ''
    ticket_count: int
    qr_alias: str

    @pydantic.root_validator()
    def validate(cls, values: dict[str, str | None]):
        if values.get('phone'):
            values['phone'] = RE_PHONE_CLEANUP.sub('', values['phone'])
        if values.get('email'):
            if not RE_EMAIL_VALIDTION.match(values['email']):
                raise ValueError("email is not valid")
        if not values.get("email") and not values['phone']:
            raise ValueError("email or phone must be specified")
        return values


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
    payload: str
