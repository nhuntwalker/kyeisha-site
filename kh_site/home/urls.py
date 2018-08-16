"""Urls routes for main site."""
from django.conf.urls import url
from django.views.generic import TemplateView
from home.views import ContactView

urlpatterns = [
    url(r'^about/$', TemplateView.as_view(template_name="base/about.html"), name="about"),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^services/therapy$', TemplateView.as_view(template_name="base/therapy.html"), name="therapy"),
    url(r'^$', TemplateView.as_view(template_name="base/index.html"), name="home"),
]
