import pydantic


class OrderBaseModel(pydantic.BaseModel):

    email: str | None = None
    phone: str | None = None
    tickets_count: int

    @pydantic.validator('email', 'phone')
    def validate_email_or_phone(cls, v, values, **kwargs):
        if not v:
            raise ValueError('email or phone must be set')
        return v


class OrderIncomeModel(OrderBaseModel):
    qr_alias: str


class OrderDatabaseModel(OrderBaseModel):
    pass
