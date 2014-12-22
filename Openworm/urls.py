from django.conf.urls import url, patterns
from Openworm import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^api/(?P<pk>[0-9]+)/$', views.OpenwormListView.as_view()),
)