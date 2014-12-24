from rest_framework import authentication, permissions
from models import *
from serializers import *
from django.shortcuts import render
from rest_framework import generics
from django.db.models import get_app, get_models

def index(request, pk='', id=-1):
    from Openworm.urls import urlpatterns #this import should be inside the function to avoid an import loop
    nice_urls = get_urls(urlpatterns) #build the list of urls recursively and then sort it alphabetically

    if (pk == '' ):
        return render(request, "Openworm/home.html", {"links":nice_urls})

    app = get_app('Openworm')
    for model in get_models(app):
        print model().get_subclass_name()
        if (pk == model().get_subclass_name()):
            model_list = model
            col_width = 100/(len(model._meta.get_all_field_names()) + 1)
            break

    print model_list

    if (id == -1):
        model_list = model_list.objects.all().values()
    else:
        model_list = model_list.objects.filter(id=id).values()

    print model_list

    return render(request, "Openworm/items.html", {"model_list":model_list, "Name":pk.title(), "col_width":col_width, "id":id, "links":nice_urls})

def get_urls(raw_urls, urlbase=''):
    '''Recursively builds a list of all the urls in the current project and the name of their associated view'''
    from operator import itemgetter
    nice_urls = []
    app = get_app('Openworm')
    for model in get_models(app):
        nice_urls.append({"pattern": model().get_subclass_name()})
    nice_urls = sorted(nice_urls, key=itemgetter('pattern')) #sort alphabetically
    return nice_urls

class ListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    #queryset = get_queryset()
    #serializer_class = AspectSerializer

    def get_queryset(self, *args, **kwargs):
        name = self.kwargs['name']
        id = self.kwargs['id']
        app = get_app('Openworm')
        for model in get_models(app):
            if (name == model().get_subclass_name()):
                model_list = model
                break
        print model_list
        return model_list.objects.filter(pk=id).values()

    def get_serializer_class(self, *args, **kwargs):
        import inspect
        import serializers
        name = self.kwargs['name']
        clsmembers = inspect.getmembers(serializers, inspect.isclass)
        for key, serializer in clsmembers:
            if (name + "Serializer" == key):
                model_list = serializer
                break
        print model_list
        return model_list

class ListViewAll(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self, *args, **kwargs):
        name = self.kwargs['name']
        app = get_app('Openworm')
        for model in get_models(app):
            print model().get_subclass_name()
            if (name == model().get_subclass_name()):
                model_list = model
                break
        print model_list
        return model_list.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        import inspect
        import serializers
        name = self.kwargs['name']
        clsmembers = inspect.getmembers(serializers, inspect.isclass)
        for key, serializer in clsmembers:
            if (name + "Serializer" == key):
                model_list = serializer
                break
        print "test"
        print model_list
        return model_list
