import uuid
from string import Template

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .messengers import send_email, send_sms
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
    email: models.CharField = models.CharField(verbose_name=_("Customer email"), blank=True, default='', max_length=50)
    phone: models.CharField = models.CharField(verbose_name=_("Customer phone"), blank=True, default='', max_length=20)
    tickets_count: models.IntegerField = models.IntegerField(verbose_name=_("Ticket count"))
    merchant_reply: models.TextField = models.TextField(verbose_name=_("Merchant reply"), blank=True, default='')
    status: models.PositiveSmallIntegerField = models.PositiveSmallIntegerField(
        verbose_name="QR Status",
        blank=True,
        choices=STATUSES,
        default=STATUS_NO_INFO,
    )
    uuid: models.UUIDField = models.UUIDField(default=uuid.uuid1, editable=False)
    qr_id: models.CharField = models.CharField(verbose_name=_("QR ID"), blank=True, default='', max_length=50)
    qr_url: models.CharField = models.CharField(verbose_name=_("QR URL"), blank=True, default='', max_length=255)
    event: models.ForeignKey = models.ForeignKey('Event', verbose_name=_('Event'), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Order #{self.id}'


@receiver(post_save, sender=Order)
def post_save(sender: type[Order], instance: Order, **kwargs):
    email_subject: str
    email_text: str
    sms_test: str
    if instance.status == Order.STATUS_SUCCESS:
        if instance.email:
            send_email(
                instance.email,
                Template(settings.SUCCESS_EMAIL_SUBJECT).substitute(event_name=instance.event.name),
                Template(settings.SUCCESS_EMAIL_TEXT).substitute(
                    event_name=instance.event.name,
                    link=f"{settings.APP_URL_BASE}/{settings.REDIRECT_URL}/{instance.uuid}",
                ),
            )
        if instance.phone:
            send_sms(
                instance.phone,
                Template(settings.SUCCESS_SMS_TEXT).substitute(
                    event_name=instance.event.name,
                    link=f"{settings.APP_URL_BASE}/{settings.REDIRECT_URL}/{instance.uuid}",
                ),
            )

    if instance.status == Order.STATUS_DECLINED:
        if instance.email:
            send_email(
                instance.email,
                Template(settings.DECLINED_EMAIL_SUBJECT).substitute(event_name=instance.event.name),
                Template(settings.DECLINED_EMAIL_TEXT).substitute(event_name=instance.event.name),
            )
        if instance.phone:
            send_sms(instance.phone, Template(settings.DECLINED_SMS_TEXT).substitute(event_name=instance.event.name))
