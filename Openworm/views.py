from rest_framework import authentication, permissions
from django.shortcuts import render
from rest_framework import generics
from django.db.models import get_app, get_models
from forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.template import RequestContext
from Openworm_Project.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
import time
from models import Platerawvideo, Plate

def index(request):
    from Openworm.urls import urlpatterns #this import should be inside the function to avoid an import loop
    nice_urls = get_urls(urlpatterns) #build the list of urls recursively and then sort it alphabetically

    return render(request, "Openworm/home.html", {"links":nice_urls})

def handle_uploaded_file(f, post):
    conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
    k = Key(bucket)
    k.key = str(time.time()) + "." + f.name
    k.set_contents_from_file(f)

    model = Platerawvideo(name = post['name'], description = post['description'], title = post['title'], shorttitle = post['shorttitle'], videofile = k.key, fps = post['fps'], numframes = post['numframes'], width = post['width'], height = post['height'], micronsperpixel = post['micronsperpixel'], platekey = Plate.objects.get(pk = post['platekey']))

    model.save()

    return model.id

def VideoUpload(request):
    from Openworm.urls import urlpatterns #this import should be inside the function to avoid an import loop
    nice_urls = get_urls(urlpatterns) #build the list of urls recursively and then sort it alphabetically

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            id = handle_uploaded_file(request.FILES['file'],request.POST)
            return HttpResponseRedirect('/dashboard/Platerawvideo/' + str(id))
    else:
        form = UploadFileForm()
    return render_to_response('Openworm/videoupload.html', {'form': form, "links":nice_urls}, context_instance=RequestContext(request))

def handle_uploaded_item(model, post):
    new_model = model()

    for key, value in post.iteritems():
        setattr(new_model, key, value)

    new_model.save()

    return new_model.id

def dashboard(request, pk='', id=-1):
    from Openworm.urls import urlpatterns #this import should be inside the function to avoid an import loop
    nice_urls = get_urls(urlpatterns) #build the list of urls recursively and then sort it alphabetically

    obj_count = {}

    app = get_app('Openworm')
    for model in get_models(app):
        obj_count[model().get_subclass_name()] = model.objects.all().count() + 1
        if (pk == model().get_subclass_name()):
            model_class = model
            model_name = model().get_subclass_name()
            col_width = 100/(len(model._meta.get_all_field_names()) + 1)
            break

    if (pk == '' ):
        return render(request, "Openworm/dashboard.html", {"links":nice_urls})

    if (id == -1):
        model_list = model_class.objects.all().values()
        return render(request, "Openworm/items.html", {"model_list":model_list, "Name":pk.title(), "col_width":col_width, "id":id, "links":nice_urls, "obj_count":obj_count[pk]})
    else:
        model_list = model_class.objects.filter(id=id).values()

        import inspect
        import forms
        clsmembers = inspect.getmembers(forms, inspect.isclass)
        for key, form in clsmembers:
            if (model_name + "Form" == key):
                form_list = form
                break

        if request.method == 'POST':
            form = form_list(request.POST)
            if form.is_valid():
                id = handle_uploaded_item(model_class,request.POST)
                return HttpResponseRedirect('/dashboard/' + model_name + '/' + str(id))
        else:
            print model_list
            if (len(model_list) > 0):
                form = form_list(initial=model_list[0])
            else:
                form = form_list()
        return render_to_response('Openworm/item.html', {'form': form, "links":nice_urls}, context_instance=RequestContext(request))


def get_urls(raw_urls, urlbase=''):
    '''Recursively builds a list of all the urls in the current project and the name of their associated view'''
    from operator import itemgetter
    nice_urls = []
    app = get_app('Openworm')
    for model in get_models(app):
        nice_urls.append({"pattern": model().get_subclass_name()})
    nice_urls = sorted(nice_urls, key=itemgetter('pattern')) #sort alphabetically
    return nice_urls

def RESTapi(request):
    from Openworm.urls import urlpatterns #this import should be inside the function to avoid an import loop
    nice_urls = get_urls(urlpatterns) #build the list of urls recursively and then sort it alphabetically

    return render(request, "Openworm/api.html", {"links":nice_urls})

class RESTListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self, *args, **kwargs):
        name = self.kwargs['name']
        id = self.kwargs['id']
        app = get_app('Openworm')
        for model in get_models(app):
            if (name == model().get_subclass_name()):
                model_list = model
                break
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
        return model_list

class RESTListViewAll(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def label_from_instance(self, obj):
        return "id: " + str(obj.id) + " name: "+ obj.name

    def get_queryset(self, *args, **kwargs):
        name = self.kwargs['name']
        app = get_app('Openworm')
        for model in get_models(app):
            if (name == model().get_subclass_name()):
                model_list = model
                break
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
        return model_list
