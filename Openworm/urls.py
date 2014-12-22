from django.conf.urls import url, patterns
from Openworm.views import *

openworm =  OpenwormListView()

urlpatterns = patterns('',
    url(r'^$', index, name='index'),

    url(r'^api/$', openworm.get(), name='api'),
)