from django.contrib import admin

from cashapp import models

def getModelFields(model) -> tuple:
    return tuple(field for field in model._meta.get_fields())


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventQRCode)
class EventQRCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass
