"""Administration for the Speaking app."""
from django.contrib import admin
from speaking.models import Presentation

FMT = '%b %d, %Y at %-I:%M %p'


def creation_date_formatter(obj):
    """Format a date."""
    return obj.date_created.strftime(FMT)


def mod_date_formatter(obj):
    """Format a date."""
    return obj.last_modified.strftime(FMT)


def image_tag(obj):
    return f'<img src="{ obj.image.url }" />'

image_tag.short_description = 'Image Preview'
image_tag.allow_tags = True


creation_date_formatter.short_description = 'Created On'
creation_date_formatter.admin_order_field = 'date_created'

mod_date_formatter.short_description = 'Last Modified On'
mod_date_formatter.admin_order_field = 'last_modified'


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    """Administration for the Presentation model."""

    empty_value_display = '-- empty --'
    date_hierarchy = 'date_created'
    list_display = ['title', creation_date_formatter, mod_date_formatter, 'order']
    fields = ['title', 'subtitle', 'image', image_tag, 'details', 'order']
    readonly_fields = [image_tag]
