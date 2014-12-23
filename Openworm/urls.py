from django.conf.urls import url, patterns
from Openworm import views
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^strains/(?P<pk>[0-9]+)/$', views.StrainListView.as_view()),
    url(r'^strains/$', views.StrainListViewAll.as_view()),

    url(r'^worms/(?P<pk>[0-9]+)/$', views.WormListView.as_view()),
    url(r'^worms/$', views.WormListViewAll.as_view()),

)