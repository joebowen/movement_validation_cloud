from django.conf.urls import url, patterns
from Openworm import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='Home'),

    url(r'^dashboard/$', views.dashboard, name='Dashboard'),
    url(r'^dashboard/(?P<pk>[\w]+)/$', views.dashboard, name='Dashboard'),
    url(r'^dashboard/(?P<pk>[\w]+)/(?P<id>[0-9]+)/$', views.dashboard, name='Dashboards'),

    url(r'^api/$', views.RESTapi, name='REST API'),
    url(r'^api/(?P<name>[\w]+)/$', views.RESTListViewAll.as_view(), name='REST API'),
    url(r'^api/(?P<name>[\w]+)/(?P<id>[0-9]+)/$', views.RESTListView.as_view(), name='REST API'),

    url(r'^init/', views.InitialData, name='Initial Data'),
)
