"""Url patterns for the group_coaching app."""
from django.conf.urls import url
from django.views.generic import TemplateView
from group_coaching.views import EventDetail


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="group_coaching/info.html"), name="group_coaching"),
    url(r'^current$', EventDetail.as_view(), name="group_coaching_event"),
]
