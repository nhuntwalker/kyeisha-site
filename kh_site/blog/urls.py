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
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', BlogView.as_view(), name="blog"),
    url(r'^add/', login_required(add_article), name='add_bpost'),
    url(r'^edit/(?P<pk>[0-9]+)/', login_required(edit_article), name='edit_bpost'),
    url(r'^delete/(?P<pk>[0-9]+)/', login_required(delete_article), name='delete_bpost'),
    url(r'^(?P<pk>\d+)/$', BlogDetail.as_view(), name="blog_detail_pk"),
    url(r'^(?P<slug>[\w\-\_]+)/$', BlogDetail.as_view(), name="blog_detail_slug"),
    url(r'^api/list/$', BlogAPIList.as_view(), name="blog_api_list")
]
