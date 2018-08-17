"""Views for group coaching."""
from django.views.generic import DetailView
from group_coaching.models import CoachingEvent


class EventDetail(DetailView):
    """View for displaying a single event's detail."""

    model = CoachingEvent
    context_object_name = 'event'
    template_name = 'group_coaching/next_event.html'

    def get_object(self, queryset=None):
        """Get the only event marked as "current"."""
        event = CoachingEvent.objects.filter(current_event=True).first()
        return event
