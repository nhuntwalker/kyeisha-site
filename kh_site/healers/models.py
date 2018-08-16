"""Models for event posts."""
from django.db import models
from django.forms import ModelForm
import datetime
from localflavor.us.models import USStateField


def _image_path(instance, filename):
    """Photo will be uploaded to media root then correct folder."""
    return "{0}/{1}".format(datetime.date.today(), filename)


class EventManager(models.Manager):
    """Define an Event Manager class."""

    def get_queryset(self):
        """Return a list of all active users."""
        qs = super(EventManager, self).get_queryset()
        return qs.all()


class Event(models.Model):
    """Create an event."""

    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=5000, blank=False)
    event_photo = models.ImageField(upload_to=_image_path, blank=True)
    date_published = models.DateTimeField(default=datetime.datetime.now)
    event_date = models.DateField()
    cost = models.CharField(max_length=50, blank=True)
    event_time = models.CharField(max_length=20, blank=True)
    objects = EventManager()


class Address(models.Model):
    """Create an address for the event."""

    event = models.OneToOneField(Event, on_delete=models.CASCADE,
                                 primary_key=True, related_name="address")
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=64, default="Seattle")
    state = USStateField(default="WA")
    zip_code = models.CharField(max_length=5)


class AddEvent(ModelForm):
    """Form class for adding aa blog article."""

    class Meta:
        """Content for blog post form."""

        model = Event
        fields = ['event_photo', 'title', 'description', 'event_date',
                  'event_time', 'cost']


class DeleteEvent(ModelForm):
    """Form class for adding an event."""

    class Meta:
        """Content for event form."""

        model = Event
        fields = []
