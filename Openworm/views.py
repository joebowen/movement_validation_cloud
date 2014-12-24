from rest_framework import authentication, permissions
from models import *
from serializers import *
from django.shortcuts import render
from rest_framework import generics

def dashboard(request):
    return render(request, "Openworm/bootstrap_dashboard.html")

def index(request):
    from Openworm.urls import urlpatterns #this import should be inside the function to avoid an import loop
    nice_urls = get_urls(urlpatterns) #build the list of urls recursively and then sort it alphabetically
    return render(request, "Openworm/links.html", {"links":nice_urls})

def get_urls(raw_urls, urlbase=''):
    '''Recursively builds a list of all the urls in the current project and the name of their associated view'''
    from operator import itemgetter
    nice_urls = []
    for entry in raw_urls:
        fullurl = (urlbase + entry.regex.pattern).replace('^','')
        fullurl = fullurl.replace('/(?P<pk>[0-9]+)/','/0/')
        fullurl = fullurl.replace('/$','/')
        fullurl = fullurl.replace('$','/')
        if entry.callback: #if it points to a view
            viewname = entry.callback.func_name
            nice_urls.append({"pattern": fullurl})
    nice_urls = sorted(nice_urls, key=itemgetter('pattern')) #sort alphabetically
    return nice_urls

class AspectListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Aspect.objects.all()
    serializer_class = AspectSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Aspect.objects.filter(pk=pk)

class AspectListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Aspect.objects.all()
    serializer_class = AspectSerializer

class BodypartListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Bodypart.objects.all()
    serializer_class = BodypartSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Bodypart.objects.filter(pk=pk)

class BodypartListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Bodypart.objects.all()
    serializer_class = BodypartSerializer

class CategoryListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Category.objects.filter(pk=pk)

class CategoryListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ComputervisionalgorithmListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Computervisionalgorithm.objects.all()
    serializer_class = ComputervisionalgorithmSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Computervisionalgorithm.objects.filter(pk=pk)

class ComputervisionalgorithmListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Computervisionalgorithm.objects.all()
    serializer_class = ComputervisionalgorithmSerializer
    
class DirectionListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Direction.objects.filter(pk=pk)

class DirectionListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    
class ExperimenterListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Experimenter.objects.all()
    serializer_class = ExperimenterSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Experimenter.objects.filter(pk=pk)

class ExperimenterListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Experimenter.objects.all()
    serializer_class = ExperimenterSerializer
    
class FeaturesperplatewireframeListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Featuresperplatewireframe.objects.all()
    serializer_class = FeaturesperplatewireframeSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Featuresperplatewireframe.objects.filter(pk=pk)

class FeaturesperplatewireframeListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Featuresperplatewireframe.objects.all()
    serializer_class = FeaturesperplatewireframeSerializer

class FeaturesperwormwireframeListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Featuresperwormwireframe.objects.all()
    serializer_class = FeaturesperwormwireframeSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Featuresperwormwireframe.objects.filter(pk=pk)

class FeaturesperwormwireframeListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Featuresperwormwireframe.objects.all()
    serializer_class = FeaturesperwormwireframeSerializer

class HistogramsperplatewireframeListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Histogramsperplatewireframe.objects.all()
    serializer_class = HistogramsperplatewireframeSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Histogramsperplatewireframe.objects.filter(pk=pk)

class HistogramsperplatewireframeListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Histogramsperplatewireframe.objects.all()
    serializer_class = HistogramsperplatewireframeSerializer
    
class HistogramsperwormwireframeListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Histogramsperwormwireframe.objects.all()
    serializer_class = HistogramsperwormwireframeSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Histogramsperwormwireframe.objects.filter(pk=pk)

class HistogramsperwormwireframeListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Histogramsperwormwireframe.objects.all()
    serializer_class = HistogramsperwormwireframeSerializer
    
class LabListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Lab.objects.all()
    serializer_class = LabSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Lab.objects.filter(pk=pk)

class LabListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Lab.objects.all()
    serializer_class = LabSerializer

class MeasurementsperwormwireframeListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Measurementsperwormwireframe.objects.all()
    serializer_class = MeasurementsperwormwireframeSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Measurementsperwormwireframe.objects.filter(pk=pk)

class MeasurementsperwormwireframeListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Measurementsperwormwireframe.objects.all()
    serializer_class = MeasurementsperwormwireframeSerializer

class PlateListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Plate.objects.all()
    serializer_class = PlateSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Plate.objects.filter(pk=pk)

class PlateListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Plate.objects.all()
    serializer_class = PlateSerializer
    
class PlatefeatureListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Platefeature.objects.all()
    serializer_class = PlatefeatureSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Platefeature.objects.filter(pk=pk)

class PlatefeatureListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Platefeature.objects.all()
    serializer_class = PlatefeatureSerializer
    
class PlaterawvideoListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Platerawvideo.objects.all()
    serializer_class = PlaterawvideoSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Platerawvideo.objects.filter(pk=pk)

class PlaterawvideoListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Platerawvideo.objects.all()
    serializer_class = PlaterawvideoSerializer
    
class PlatewireframevideoListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Platewireframevideo.objects.all()
    serializer_class = PlatewireframevideoSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Platewireframevideo.objects.filter(pk=pk)

class PlatewireframevideoListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Platewireframevideo.objects.all()
    serializer_class = PlatewireframevideoSerializer
    
class SignListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Sign.objects.all()
    serializer_class = SignSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Sign.objects.filter(pk=pk)

class SignListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Sign.objects.all()
    serializer_class = SignSerializer
    
class StrainListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Strain.objects.all()
    serializer_class = StrainSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Strain.objects.filter(pk=pk)

class StrainListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Strain.objects.all()
    serializer_class = StrainSerializer
    
class TypeListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Type.objects.filter(pk=pk)

class TypeListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    
class VideoattributesListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Videoattributes.objects.all()
    serializer_class = VideoattributesSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Videoattributes.objects.filter(pk=pk)

class VideoattributesListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Videoattributes.objects.all()
    serializer_class = VideoattributesSerializer
    
class WormListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Worm.objects.all()
    serializer_class = WormSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Worm.objects.filter(pk=pk)

class WormListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Worm.objects.all()
    serializer_class = WormSerializer
    
class WormfeatureListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Wormfeature.objects.all()
    serializer_class = WormfeatureSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Wormfeature.objects.filter(pk=pk)

class WormfeatureListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Wormfeature.objects.all()
    serializer_class = WormfeatureSerializer
    
class WorminteractionListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Worminteraction.objects.all()
    serializer_class = WorminteractionSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Worminteraction.objects.filter(pk=pk)

class WorminteractionListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Worminteraction.objects.all()
    serializer_class = WorminteractionSerializer
    
class WormlistListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Wormlist.objects.all()
    serializer_class = WormlistSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Wormlist.objects.filter(pk=pk)

class WormlistListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Wormlist.objects.all()
    serializer_class = WormlistSerializer
    
class WormmeasurementListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Wormmeasurement.objects.all()
    serializer_class = WormmeasurementSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Wormmeasurement.objects.filter(pk=pk)

class WormmeasurementListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Wormmeasurement.objects.all()
    serializer_class = WormmeasurementSerializer
    
class WormwireframevideoListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Wormwireframevideo.objects.all()
    serializer_class = WormwireframevideoSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Wormwireframevideo.objects.filter(pk=pk)

class WormwireframevideoListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Wormwireframevideo.objects.all()
    serializer_class = WormwireframevideoSerializer
    
