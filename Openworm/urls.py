from django.conf.urls import url, patterns
from Openworm.views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),

    url(r'^api/$', OpenwormListView().get, name='api'),
)