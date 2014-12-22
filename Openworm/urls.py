from django.conf.urls import url
from views import MyView

myview = MyView()

urlpatterns = [
    url(r'^$', myview.index, name='index'),

    url(r'^api/$', myview.openworm_list),
    url(r'^api/(?P<pk>[0-9]+)/$', myview.openworm_detail),
]