import typing

from django.contrib import admin
from django.http import HttpRequest

from cashapp import models


class BasicAdmin(admin.ModelAdmin):
    """Base admin."""

    show_in_dashboard: bool = True
    full_readonly_mode: bool = False
    actions: list[str] = [
        'delete_selected',
    ]

    def get_changeform_initial_data(self, request: HttpRequest) -> dict:
        """Pass last base as initial value (this helps to preselect correct
        base in dropdowns)"""
        initial_data: dict = super().get_changeform_initial_data(request)
        if '_changelist_filters' in initial_data:
            query_parts: list = initial_data['_changelist_filters'].split('=')
            if len(query_parts) == 2 and query_parts[0] in ('base__id', 'base__id__exact', 'base_id'):
                initial_data['base'] = query_parts[1]
        if 'base' not in initial_data:
            last_base: models.Base | None = request.session.get('visited_base_last')
            if last_base:
                initial_data['base'] = last_base
        return initial_data

    def get_readonly_fields(
        self, request: HttpRequest, obj: typing.Any | None = None
    ) -> list[str] | tuple[typing.Any, ...]:  # type: ignore
        """Readonly all + next view."""
        if self.full_readonly_mode:
            return list(
                [field.name for field in self.opts.local_fields]
                + [field.name for field in self.opts.local_many_to_many]
            )
        return super().get_readonly_fields(request, obj)  # type: ignore

    def change_view(
        self,
        request: HttpRequest,
        object_id: typing.Any,
        form_url: str = '',
        extra_context: dict | None = None,
    ) -> typing.Any:
        """Override change view for full readonly mode (disable save buttons
        completely)"""
        if self.full_readonly_mode:
            extra_context = extra_context or {}
            extra_context['show_save_and_continue'] = False
            extra_context['show_save'] = False
        return super().change_view(request, object_id, extra_context=extra_context)

    def has_module_permission(self, request: HttpRequest) -> bool:
        """Hide model class in dashboard."""
        return self.show_in_dashboard


class BasicHistoryAdmin(BasicAdmin):
    """This model exposes created/modified fields."""

    custom_readonly_fields: list = []
    custom_fields_pre: list = []

    def get_readonly_fields(self, request: HttpRequest, obj: typing.Any | None = None) -> list:
        """Override of readonly_fields property to expose created/modified
        fields."""
        regular_state: list = list(super().get_readonly_fields(request, obj))
        if not self.full_readonly_mode:
            return (
                regular_state
                + self.custom_readonly_fields
                + [
                    'created',
                    'modified',
                ]
            )
        return regular_state + self.custom_readonly_fields

    def get_fields(self, request: HttpRequest, obj: typing.Any | None = None) -> list:
        """Override to allow reorder fieldsets."""
        original_fields: list = list(super().get_fields(request, obj))
        if original_fields:
            for one_field in self.custom_fields_pre:
                original_fields.remove(one_field)
            original_fields = self.custom_fields_pre + original_fields
        return original_fields


@admin.register(models.Organization)
class OrganizationAdmin(BasicHistoryAdmin):
    ordering: tuple = ('-created',)
    search_fields = ('name',)
    list_filter = (
        'created',
        'name',
    )
    list_display: tuple = (
        'name',
        'description',
    )
    list_display_links: tuple = ('name',)


@admin.register(models.Event)
class EventAdmin(BasicHistoryAdmin):
    ordering: tuple = ('-created',)
    search_fields = (
        'name',
        'organization',
    )
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
class EventQRCodeAdmin(BasicHistoryAdmin):
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
class OrderAdmin(BasicHistoryAdmin):
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
