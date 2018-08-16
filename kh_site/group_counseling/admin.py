"""Administration for the Group Coaching app."""
from django.contrib import admin
from group_coaching.models import CoachingEvent, DATE_FMT

TIME_FMT = '%-I:%M %p'


def start_date_formatter(obj):
    """."""
    return obj.start_date.strftime(DATE_FMT)

start_date_formatter.short_description = 'Starting Date'


def end_date_formatter(obj):
    """."""
    return obj.end_date.strftime(DATE_FMT)

end_date_formatter.short_description = 'Ending Date'


@admin.register(CoachingEvent)
class CoachingEventAdmin(admin.ModelAdmin):
    """Administration of the Coaching Event model."""

    fields = [
        'start_date', 'end_date', 'meeting_days', 'current_event',
        'start_time', 'end_time', 'cost', 'external_link', 'location',
        'logistics', 'outline'
    ]
    list_display = [start_date_formatter, end_date_formatter, 'current_event', 'location']
    date_hierarchy = 'start_date'
    empty_value_display = "-- empty --"
