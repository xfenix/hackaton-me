import uuid

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
    merchant_id: models.TextField = models.TextField(verbose_name=_("Merchant id"), default='')

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


class Order(DateHistoryModel):
    STATUS_SUCCESS: int = 1
    STATUS_DECLINED: int = 2
    STATUS_NO_INFO: int = 3
    STATUS_IN_PROGRESS: int = 3
    STATUSES: tuple = (
        (STATUS_SUCCESS, _('Success')),
        (STATUS_DECLINED, _('Declined')),
        (STATUS_NO_INFO, _('No info')),
        (STATUS_IN_PROGRESS, _('In progress')),
    )
    STATUS_MAP: dict = {
        "SUCCESS": STATUS_SUCCESS,
        "DECLINED": STATUS_DECLINED,
        "NO_INFO": STATUS_NO_INFO,
        "IN_PROGRESS": STATUS_IN_PROGRESS,
    }
    email: models.TextField = models.TextField(verbose_name=_("Customer email"), blank=True, default='')
    phone: models.TextField = models.TextField(verbose_name=_("Customer phone"), blank=True, default='')
    tickets_count: models.TextField = models.TextField(verbose_name=_("Ticket count"))
    merchant_reply: models.TextField = models.TextField(verbose_name=_("Merchant reply"), blank=True, default='')
    status: models.TextField = models.PositiveSmallIntegerField(
        verbose_name="QR Status",
        blank=True,
        choices=STATUSES,
        default=STATUS_NO_INFO,
    )
    uuid: models.UUIDField = models.UUIDField(default=uuid.uuid1, editable=False)
    qr_id: models.TextField = models.TextField(verbose_name=_("QR ID"), blank=True, default='')
    qr_url: models.TextField = models.TextField(verbose_name=_("QR URL"), blank=True, default='')
    event: models.ForeignKey = models.ForeignKey('Event', verbose_name=_('Event'), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Order #{self.id}'
