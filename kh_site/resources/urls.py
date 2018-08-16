from django.conf.urls import url
from resources.views import ResourceView


urlpatterns = [
    url(
        r'^$',
        ResourceView.as_view(),
        name="resources"
    ),
]