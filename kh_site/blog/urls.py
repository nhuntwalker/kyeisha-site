"""Urls routes for main site."""
from django.conf.urls import url
from blog.views import (
    add_article,
    BlogView,
    BlogAPIList,
    BlogDetail,
    edit_article,
    delete_article
)

urlpatterns = [
    url(r'^$', BlogView.as_view(), name="blog"),
    url(r'^(?P<pk>\d+)/$', BlogDetail.as_view(), name="blog_detail_pk"),
    url(r'^(?P<slug>[\w\-\_]+)/$', BlogDetail.as_view(), name="blog_detail_slug"),
    url(r'^api/list/$', BlogAPIList.as_view(), name="blog_api_list")
]
