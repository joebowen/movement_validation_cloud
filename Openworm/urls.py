from django.conf.urls import url
from Openworm.views import *



urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^api/$', OpenwormListView().get()),
]