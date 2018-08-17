"""Healer app urls."""
from django.conf.urls import url
from django.views.generic import TemplateView
from healers.views import add_event, edit_event, play_view, delete_event
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="healers/healers.html"), name="healing_healers"),
]
