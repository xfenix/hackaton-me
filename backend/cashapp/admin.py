from django.contrib import admin

from cashapp import models


def getModelFields(model) -> tuple:
    return tuple(field for field in model._meta.get_fields())


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display: tuple = (
        'name',
        'description',
    )


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = (
        'created',
        'name',
    )
    list_display: tuple = (
        'name',
        'event_date',
        'organization',
    )
    list_display_links: tuple = ('name',)


@admin.register(models.EventQRCode)
class EventQRCodeAdmin(admin.ModelAdmin):
    ordering: tuple = ('-created',)
    search_fields = ('event',)
    list_filter = (
        'alias',
        'event',
    )
    list_display: tuple = (
        'alias',
        'description',
        'price',
        'event',
    )
    list_display_links: tuple = ('alias',)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    ordering: tuple = ('-created',)
    search_fields = (
        'email',
        'phone',
        'event',
        'status',
    )
    list_filter = (
        'email',
        'phone',
        'event',
        'status',
    )
    list_display: tuple = (
        'email',
        'phone',
        'tickets_count',
        'merchant_reply',
        'status',
        'event',
    )
    list_display_links: tuple = (
        'email',
        'phone',
    )
