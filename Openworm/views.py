from rest_framework import authentication, permissions
from django.shortcuts import render
from rest_framework import generics
from django.db.models import get_app, get_models
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.template import RequestContext
from Openworm_Project.settings import AWS_STORAGE_BUCKET_NAME
import time
import re
from models import Plate, Lab, Experimenter, Strain, Worm, Wormlist

def index(request):
    nice_urls = get_urls()

    return render(request, "Openworm/home.html", {"links":nice_urls})

def InitialData(request):
    model = Lab(name = "Test Name", description = "Test Description", address = "Test Address")
    model.save()
    lab_id = model.id

    model = Experimenter(labkey = Lab.objects.get(pk = lab_id), name = "Test Name", description = "Test Description")
    model.save()
    experimenter_id = model.id

    model = Strain(name = "Test Name", gene = "Test Gene", genotype = "Test Genotype", allele = "Test Allele", chromosome = "Test Chomosome", simulated = "Y")
    model.save()
    strain_id = model.id

    model = Worm(strainkey = Strain.objects.get(pk = strain_id), name = "Test Name", sex = "Test Sex", generationssincethawing = 3, habituation = "Test Habituation")
    model.save()
    worm_id = model.id

    model = Wormlist(wormkey = Worm.objects.get(pk = worm_id), name = "Test Name")
    model.save()
    wormlist_id = model.id

    model = Plate(wormlistkey = Wormlist.objects.get(pk = wormlist_id), experimenterkey = Experimenter.objects.get(pk = experimenter_id), name = "Test Name", sampletype = "Test Type", copyright = "Test Copyright", vulvaorientation = "Test", annotation = "Test Annotation", chemicals = "Test Chemicals", food = "Test Food", illumination = "Test Illumination", temperature = 10, tracker = "Test Tracker", agarside = "Test Agar Side", gasconcentration = "Test Gas Concentration")
    model.save()
    plate_id = model.id

    return HttpResponse(plate_id)

def handle_uploaded_item(request, model, post):
    new_model = model()

    for key, value in post.iteritems():
        if "videofile" in key:
            conn = S3Connection()
            bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
            k = Key(bucket)
            k.key = str(time.time()) + "." + request.FILES['file'].name
            k.set_contents_from_file(request.FILES['file'])
            setattr(new_model, key, k.key)
        elif "key" not in key:
            setattr(new_model, key, value)
        else:
            app = get_app('Openworm')
            for model in get_models(app):
                p = re.compile('(\w*)key')
                model_name = p.match(key).group(1).title()
                if (model_name == model().get_subclass_name()):
                    print model_name
                    setattr(new_model, key, model.objects.get(pk = value))

    new_model.save()

    return new_model.id

def dashboard(request, pk='', id=-1):
    nice_urls = get_urls()

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
                id = handle_uploaded_item(request, model_class, request.POST)
                return HttpResponseRedirect('/dashboard/' + model_name + '/' + str(id))
        else:
            if (len(model_list) > 0):
                form = form_list(initial=model_list[0])
            else:
                form = form_list()
        return render_to_response('Openworm/item.html', {'form': form, "links":nice_urls}, context_instance=RequestContext(request))


def get_urls():
    '''Recursively builds a list of all the urls in the current project and the name of their associated view'''
    from operator import itemgetter
    nice_urls = []
    app = get_app('Openworm')
    for model in get_models(app):
        nice_urls.append({"pattern": model().get_subclass_name()})
    nice_urls = sorted(nice_urls, key=itemgetter('pattern')) #sort alphabetically
    return nice_urls

def RESTapi(request):
    nice_urls = get_urls()

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
