from django.conf.urls import url, patterns
from Openworm import views
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^Aspects/(?P<pk>[0-9]+)/$', views.AspectListView.as_view()),
    url(r'^Aspects/$', views.AspectListViewAll.as_view()),

    url(r'^Bodyparts/(?P<pk>[0-9]+)/$', views.BodypartListView.as_view()),
    url(r'^Bodyparts/$', views.BodypartListViewAll.as_view()),

    url(r'^Categories/(?P<pk>[0-9]+)/$', views.CategoryListView.as_view()),
    url(r'^Categories/$', views.CategoryListViewAll.as_view()),

    url(r'^Computervisionalgorithms/(?P<pk>[0-9]+)/$', views.ComputervisionalgorithmListView.as_view()),
    url(r'^Computervisionalgorithms/$', views.ComputervisionalgorithmListViewAll.as_view()),

    url(r'^Directions/(?P<pk>[0-9]+)/$', views.DirectionListView.as_view()),
    url(r'^Directions/$', views.DirectionListViewAll.as_view()),

    url(r'^Experimenters/(?P<pk>[0-9]+)/$', views.ExperimenterListView.as_view()),
    url(r'^Experimenters/$', views.ExperimenterListViewAll.as_view()),
    
    url(r'^Featuresperplatewireframes/(?P<pk>[0-9]+)/$', views.FeaturesperplatewireframeListView.as_view()),
    url(r'^Featuresperplatewireframes/$', views.FeaturesperplatewireframeListViewAll.as_view()),
    
    url(r'^Featuresperwormwireframes/(?P<pk>[0-9]+)/$', views.FeaturesperwormwireframeListView.as_view()),
    url(r'^Featuresperwormwireframes/$', views.FeaturesperwormwireframeListViewAll.as_view()),
    
    url(r'^Histogramsperplatewireframes/(?P<pk>[0-9]+)/$', views.HistogramsperplatewireframeListView.as_view()),
    url(r'^Histogramsperplatewireframes/$', views.HistogramsperplatewireframeListViewAll.as_view()),
    
    url(r'^Histogramsperwormwireframes/(?P<pk>[0-9]+)/$', views.HistogramsperwormwireframeListView.as_view()),
    url(r'^Histogramsperwormwireframes/$', views.HistogramsperwormwireframeListViewAll.as_view()),
    
    url(r'^Labs/(?P<pk>[0-9]+)/$', views.LabListView.as_view()),
    url(r'^Labs/$', views.LabListViewAll.as_view()),
    
    url(r'^Measurementsperwormwireframes/(?P<pk>[0-9]+)/$', views.MeasurementsperwormwireframeListView.as_view()),
    url(r'^Measurementsperwormwireframes/$', views.MeasurementsperwormwireframeListViewAll.as_view()),
    
    url(r'^Plates/(?P<pk>[0-9]+)/$', views.PlateListView.as_view()),
    url(r'^Plates/$', views.PlateListViewAll.as_view()),
    
    url(r'^Platefeatures/(?P<pk>[0-9]+)/$', views.PlatefeatureListView.as_view()),
    url(r'^Platefeatures/$', views.PlatefeatureListViewAll.as_view()),
    
    url(r'^Platerawvideos/(?P<pk>[0-9]+)/$', views.PlaterawvideoListView.as_view()),
    url(r'^Platerawvideos/$', views.PlaterawvideoListViewAll.as_view()),
    
    url(r'^Platewireframevideos/(?P<pk>[0-9]+)/$', views.PlatewireframevideoListView.as_view()),
    url(r'^Platewireframevideos/$', views.PlatewireframevideoListViewAll.as_view()),
    
    url(r'^Signs/(?P<pk>[0-9]+)/$', views.SignListView.as_view()),
    url(r'^Signs/$', views.SignListViewAll.as_view()),
    
    url(r'^Strains/(?P<pk>[0-9]+)/$', views.StrainListView.as_view()),
    url(r'^Strains/$', views.StrainListViewAll.as_view()),
    
    url(r'^Types/(?P<pk>[0-9]+)/$', views.TypeListView.as_view()),
    url(r'^Types/$', views.TypeListViewAll.as_view()),
    
    url(r'^Videoattributes/(?P<pk>[0-9]+)/$', views.VideoattributesListView.as_view()),
    url(r'^Videoattributes/$', views.VideoattributesListViewAll.as_view()),
    
    url(r'^Worms/(?P<pk>[0-9]+)/$', views.WormListView.as_view()),
    url(r'^Worms/$', views.WormListViewAll.as_view()),
    
    url(r'^Wormfeatures/(?P<pk>[0-9]+)/$', views.WormfeatureListView.as_view()),
    url(r'^Wormfeatures/$', views.WormfeatureListViewAll.as_view()),
    
    url(r'^Worminteractions/(?P<pk>[0-9]+)/$', views.WorminteractionListView.as_view()),
    url(r'^Worminteractions/$', views.WorminteractionListViewAll.as_view()),
    
    url(r'^Wormlists/(?P<pk>[0-9]+)/$', views.WormlistListView.as_view()),
    url(r'^Wormlists/$', views.WormlistListViewAll.as_view()),
    
    url(r'^Wormmeasurements/(?P<pk>[0-9]+)/$', views.WormmeasurementListView.as_view()),
    url(r'^Wormmeasurements/$', views.WormmeasurementListViewAll.as_view()),
    
    url(r'^Wormwireframevideos/(?P<pk>[0-9]+)/$', views.WormwireframevideoListView.as_view()),
    url(r'^Wormwireframevideos/$', views.WormwireframevideoListViewAll.as_view()),
)
