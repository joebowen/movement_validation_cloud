from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from Openworm import urls as openworm

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(openworm)),
)
