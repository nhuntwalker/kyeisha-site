"""Healer app urls."""
from django.conf.urls import url
from django.views.generic import TemplateView
from healers.views import add_event, edit_event, play_view, delete_event
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^play/$', play_view, name="play"),
    url(r'^dance/$', TemplateView.as_view(template_name="beyonce.html"), name="beyonce"),
    url(r'^add/', login_required(add_event), name='add_event'),
    url(r'^edit/(?P<pk>[0-9]+)/', login_required(edit_event), name='edit_event'),
    url(r'^delete/(?P<pk>[0-9]+)/', login_required(delete_event), name='delete_event'),
    url(r'^$', TemplateView.as_view(template_name="healers/healers.html"), name="healing_healers"),
]
