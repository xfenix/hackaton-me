from django.db import models
from django.utils.translation import gettext_lazy as _


class DateHistoryModel(models.Model):
    """Abstract model with create/change date fields."""

    created: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name=_('Created time'))
    modified: models.DateTimeField = models.DateTimeField(auto_now=True, verbose_name=_('Modified time'))

    class Meta:
        abstract = True


class Organization(DateHistoryModel):
    name: models.TextField = models.TextField(verbose_name=_("Organization name"))
    description: models.TextField = models.TextField(verbose_name=_("Organization description"))
    merchant_id: models.TextField = models.TextField(verbose_name=_("Merchant id"))

    def __str__(self) -> str:
        return self.name


class Event(DateHistoryModel):
    description: models.TextField = models.TextField(verbose_name=_("Event description"))
    name: models.TextField = models.TextField(verbose_name=_("Event name"))
    background: models.TextField = models.TextField(verbose_name=_("Event background"))
    logo: models.TextField = models.TextField(verbose_name=_("Event logo"))
    event_date: models.DateTimeField = models.DateTimeField(verbose_name=_('Event date and time'))
    organization: models.ForeignKey = models.ForeignKey(
        'Organization', verbose_name=_('Organization'), on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class EventQRCode(DateHistoryModel):
    alias: models.TextField = models.TextField(verbose_name=_("QR Code alias"), unique=True)
    description: models.TextField = models.TextField(verbose_name=_("QR Code description"))
    price: models.TextField = models.TextField(verbose_name=_("Event price"))
    event: models.ForeignKey = models.ForeignKey('Event', verbose_name=_('Event'), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.alias


class SBPQRCode(DateHistoryModel):
    qr_id: models.TextField = models.TextField(verbose_name=_("QR ID"))
    qr_status: models.TextField = models.TextField(verbose_name="QR Status")
    qr_url: models.TextField = models.TextField(verbose_name=_("QR URL"))
    order: models.ForeignKey = models.ForeignKey('Order', verbose_name=_("Order"))


class Order(DateHistoryModel):
    email: models.TextField = models.TextField(verbose_name=_("Customer email"))
    phone: models.TextField = models.TextField(verbose_name=_("Customer phone"))
    tickets_count: models.TextField = models.TextField(verbose_name=_("Ticket count"))
    merchant_reply: models.TextField = models.TextField(verbose_name=_("Merchant reply"))
    status: models.TextField = models.TextField(verbose_name=_("Order status"))
    event: models.ForeignKey = models.ForeignKey('Event', verbose_name=_('Event'), on_delete=models.CASCADE)
    uuid: models.UUIDField(default=uuid.uuid1, editable=False)

    def __str__(self) -> str:
        return f'Order #{self.id}'
