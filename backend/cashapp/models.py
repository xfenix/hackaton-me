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
    alias: models.TextField = models.TextField(verbose_name=_("QR Code alias"))
    description: models.TextField = models.TextField(verbose_name=_("QR Code description"))
    price: models.TextField = models.TextField(verbose_name=_("Event price"))
    event: models.ForeignKey = models.ForeignKey('Event', verbose_name=_('Event'), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.alias


class Order(DateHistoryModel):
    email: models.TextField = models.TextField(verbose_name=_("Customer email"))
    phone: models.TextField = models.TextField(verbose_name=_("Customer phone"))
    tickets_count: models.TextField = models.TextField(verbose_name=_("Ticket count"))
    merchant_reply: models.TextField = models.TextField(verbose_name=_("Merchant reply"))
    status: models.TextField = models.TextField(verbose_name=_("Order status"))
    event: models.ForeignKey = models.ForeignKey('Event', verbose_name=_('Event'), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Order #{self.id}'
