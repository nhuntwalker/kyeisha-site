"""Url patterns for the group_coaching app."""
from django.conf.urls import url
from group_coaching.views import EventDetail


urlpatterns = [
    url(
        r'^$',
        EventDetail.as_view(),
        name="group_coaching"
    ),
]
