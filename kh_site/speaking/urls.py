from django.conf.urls import url
from speaking.views import (
    PresentationsList,
    PresentationsJSONList,
    PresentationDetail
)


urlpatterns = [
    url(r'^$', PresentationsList.as_view(), name="speaking"),
    url(r'^api/list/$', PresentationsJSONList.as_view(), name="speaking_json"),
    url(r'^api/detail/(?P<pk>[0-9]+)/$', PresentationDetail.as_view(), name='speaking_detail')
]
