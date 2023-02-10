import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils import make_django_title_list_from_tuple


class DateHistoryModel(models.Model):
    """Abstract model with create/change date fields."""

    created: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name=_('Created time'))
    modified: models.DateTimeField = models.DateTimeField(auto_now=True, verbose_name=_('Modified time'))

    class Meta:
        abstract = True


class Organization(DateHistoryModel):
    name: models.CharField = models.CharField(verbose_name=_("Organization name"), max_length=100)
    description: models.TextField = models.TextField(verbose_name=_("Organization description"))
    merchant_id: models.CharField = models.CharField(verbose_name=_("Merchant id"), default='', max_length=50)

    def __str__(self) -> str:
        return self.name


class Event(DateHistoryModel):
    name: models.CharField = models.CharField(verbose_name=_("Event name"), max_length=255)
    description: models.TextField = models.TextField(verbose_name=_("Event description"))
    background: models.CharField = models.CharField(
        verbose_name=_("Event background"),
        max_length=255,
        default=make_django_title_list_from_tuple(settings.BACKGROUND_CHOICES)[0],
        choices=make_django_title_list_from_tuple(settings.BACKGROUND_CHOICES),
    )
    logo: models.CharField = models.CharField(
        verbose_name=_("Event logo"),
        max_length=255,
        default=make_django_title_list_from_tuple(settings.LOGO_CHOICES)[0],
        choices=make_django_title_list_from_tuple(settings.LOGO_CHOICES),
    )
    event_date: models.DateTimeField = models.DateTimeField(verbose_name=_('Event date and time'))
    organization: models.ForeignKey = models.ForeignKey(
        'Organization', verbose_name=_('Organization'), on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class EventQRCode(DateHistoryModel):
    alias: models.CharField = models.CharField(verbose_name=_("QR Code alias"), unique=True, max_length=100)
    description: models.TextField = models.TextField(verbose_name=_("QR Code description"))
    price: models.CharField = models.CharField(verbose_name=_("Event price"), max_length=30)
    event: models.ForeignKey = models.ForeignKey('Event', verbose_name=_('Event'), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.alias


class Order(DateHistoryModel):
    email: models.CharField = models.CharField(verbose_name=_("Customer email"), blank=True, default='', max_length=30)
    phone: models.CharField = models.CharField(verbose_name=_("Customer phone"), blank=True, default='', max_length=16)
    tickets_count: models.CharField = models.CharField(verbose_name=_("Ticket count"), max_length=5)
    merchant_reply: models.TextField = models.TextField(verbose_name=_("Merchant reply"), blank=True, default='')
    status: models.CharField = models.CharField(verbose_name=_("Order status"), blank=True, default='', max_length=20)
    uuid: models.UUIDField = models.UUIDField(default=uuid.uuid1, editable=False)
    qr_id: models.CharField = models.CharField(verbose_name=_("QR ID"), blank=True, default='', max_length=30)
    qr_status: models.CharField = models.CharField(verbose_name="QR Status", blank=True, default='', max_length=30)
    qr_url: models.CharField = models.CharField(verbose_name=_("QR URL"), blank=True, default='', max_length=255)
    event: models.ForeignKey = models.ForeignKey('Event', verbose_name=_('Event'), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Order #{self.id}'
