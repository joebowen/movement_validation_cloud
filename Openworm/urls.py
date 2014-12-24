from django.conf.urls import url, patterns
from Openworm import views
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^$', views.index, name='Dashboard'),

    url(r'^dashboard/$', views.index, name='Dashboard'),
    url(r'^dashboard/(?P<pk>[\w]+)/$', views.index, name='Dashboard'),
    url(r'^dashboard/(?P<pk>[\w]+)/(?P<id>[0-9]+)/$', views.index, name='Dashboards'),

    url(r'^api/$', views.index, name='Dashboard'),
    url(r'^api/(?P<name>[\w]+)/$', views.ListViewAll.as_view()),
    url(r'^api/(?P<name>[\w]+)/(?P<id>[0-9]+)/$', views.ListView.as_view()),
)
