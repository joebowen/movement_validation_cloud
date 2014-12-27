from django.conf.urls import url, patterns, include
from Openworm import views, forms
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^$', views.index, name='Home'),

    url(r'^dashboard/$', views.dashboard, name='Dashboard'),
    url(r'^dashboard/(?P<pk>[\w]+)/$', views.dashboard, name='Dashboard'),
    url(r'^dashboard/(?P<pk>[\w]+)/(?P<id>[0-9]+)/$', views.dashboard, name='Dashboards'),

    url(r'^api/$', views.api, name='REST API'),
    url(r'^api/(?P<name>[\w]+)/$', views.ListViewAll.as_view(), name='REST API'),
    url(r'^api/(?P<name>[\w]+)/(?P<id>[0-9]+)/$', views.ListView.as_view(), name='REST API'),

    url(r'^videoupload/', views.VideoUpload, name='Video Upload'),
)
