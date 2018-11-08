"""kh_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^manage/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^services/speaking/', include('speaking.urls')),
    url(r'^services/healers/', include('healers.urls')),
    url(r'^services/groups/', include('group_coaching.urls')),
    url(r'^services/resources/', include('resources.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'

admin.site.site_title = "Kyeisha Hodge admin"
admin.site.site_header = "Kyeisha Hodge - Administration"

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
