from django import forms
from models import *

class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "id: " + str(obj.id) + " name: "+ obj.name

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    shorttitle = forms.CharField(max_length=20)
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    fps = forms.IntegerField()
    numframes = forms.IntegerField()
    width = forms.IntegerField()
    height = forms.IntegerField()
    micronsperpixel = forms.IntegerField()
    platekey = MyModelChoiceField(queryset=Plate.objects.all())
    file  = forms.FileField()

class WormForm(forms.Form):
    wormkey = MyModelChoiceField(queryset=Worm.objects.all())
    timestamp =  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    
    
    
    
class AspectForm(forms.Form):
    aspectkey = forms.IntegerField()
    timestamp=  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)


class BodypartForm(forms.Form):
    bodypartkey = forms.IntegerField()
    timestamp=  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    startskeletonindex = forms.FloatField()
    endskeletonindex = forms.FloatField()
    startskeletonindexdeprecated = forms.FloatField()
    endskeletonindexdeprecated = forms.FloatField()


class CategoryForm(forms.Form):
    categorykey = forms.IntegerField()
    timestamp=  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)


class ComputervisionalgorithmForm(forms.Form):
    cvalgorithmkey = forms.IntegerField()
    timestamp=  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    framebyframe = forms.CharField(max_length=1)
    author = forms.CharField(max_length=20)
    academicpaper = forms.CharField(max_length=20)
    code = forms.CharField(max_length=100)


class DirectionForm(forms.Form):
    directionkey = forms.IntegerField()
    
    timestamp =  forms.DateTimeField()
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=500)
   
class ExperimenterForm(forms.Form):
    experimenterkey = forms.IntegerField()
    labkey = MyModelChoiceField(queryset=Lab.objects.all())
    timestamp =  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    timestamp =  forms.DateTimeField()


class FeaturesperplatewireframeForm(forms.Form):
    featuresperplatewireframe = forms.IntegerField()
    platefeaturekey = MyModelChoiceField(queryset=Platefeature.objects.all())
    timestamp =  forms.DateTimeField()
    value = forms.CharField(max_length=500)
    platewireframevideokey = MyModelChoiceField(queryset=Platewireframevideo.objects.all())


class FeaturesperwormwireframeForm(forms.Form):
    featuresperwormwireframekey = forms.IntegerField()
    wormfeaturekey = MyModelChoiceField(queryset=Wormfeature.objects.all())
    wormwireframekey = MyModelChoiceField(queryset=Wormwireframevideo.objects.all())
    timestamp =  forms.DateTimeField()
    value = forms.CharField(max_length=500)


class HistogramsperplatewireframeForm(forms.Form):
    histogramsperplatewireframekey = forms.IntegerField()
    platewireframevideokey = MyModelChoiceField(queryset=Platewireframevideo.objects.all())
    timestamp =  forms.DateTimeField()
    bins = forms.CharField(max_length=500)
    counts = forms.CharField(max_length=500)


class HistogramsperwormwireframeForm(forms.Form):
    histogramsperwormwireframekey = forms.IntegerField()
    eventdirectionkey = MyModelChoiceField(queryset=Direction.objects.all())
    wormfeaturekey = MyModelChoiceField(queryset=Wormfeature.objects.all())
    wormwireframekey = MyModelChoiceField(queryset=Wormwireframevideo.objects.all())
    signkey = MyModelChoiceField(queryset=Sign.objects.all())
    timestamp =  forms.DateTimeField()
    bins = forms.CharField(max_length=500)
    counts = forms.CharField(max_length=500)


class LabForm(forms.Form):
    labkey = forms.IntegerField()
    timestamp=  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    address = forms.CharField(max_length=20)


class MeasurementsperwormwireframeForm(forms.Form):
    measurementsperwormwireframe = forms.IntegerField()
    wormmeasurementkey = MyModelChoiceField(queryset=Wormmeasurement.objects.all())
    wormwireframekey = MyModelChoiceField(queryset=Wormwireframevideo.objects.all())
    timestamp =  forms.DateTimeField()
    value = forms.CharField(max_length=500)


class PlateForm(forms.Form):
    platekey = forms.IntegerField()
    experimenterkey = MyModelChoiceField(queryset=Experimenter.objects.all())
    wormlistkey = MyModelChoiceField(queryset=Wormlist.objects.all())
    def get_subclass_name(self):
        return self.__class__.__name__

    name = forms.CharField(max_length=100)
    timestamp =  forms.DateTimeField()
    sampletype = forms.CharField(max_length=18)
    startdatetime = forms.DateTimeField()
    copyright = forms.CharField(max_length=20)
    vulvaorientation = forms.CharField(max_length=20)
    annotation = forms.CharField(max_length=20)
    chemicals = forms.CharField(max_length=20)
    food = forms.CharField(max_length=20)
    illumination = forms.CharField(max_length=20)
    temperature = forms.IntegerField()
    tracker = forms.CharField(max_length=20)
    agarside = forms.CharField(max_length=20)
    gasconcentration = forms.CharField(max_length=500)


class PlatefeatureForm(forms.Form):
    platefeaturekey = forms.IntegerField()
    timestamp=  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    title = forms.CharField(max_length=20)
    shorttitle = forms.CharField(max_length=20)


class PlaterawvideoForm(forms.Form):
    platerawvideokey = forms.IntegerField()
    platekey = MyModelChoiceField(queryset=Plate.objects.all())    
    timestamp =  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    title = forms.CharField(max_length=20)
    shorttitle = forms.CharField(max_length=20)
    videofile = S3DirectField(dest='destination_key_from_settings')
    fps = forms.IntegerField()
    numframes = forms.FloatField()
    width = forms.IntegerField()
    height = forms.IntegerField()
    micronsperpixel = forms.IntegerField()


class PlatewireframevideoForm(forms.Form):
    platewireframevideokey = forms.IntegerField()
    platerawvideokey = MyModelChoiceField(queryset=Platerawvideo.objects.all())
    cvalgorithmkey = MyModelChoiceField(queryset=Computervisionalgorithm.objects.all())
    timestamp =  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    wireframevideo = forms.CharField(max_length=500)
    droppedframeinfo = forms.CharField(max_length=500)


class SignForm(forms.Form):
    signkey = forms.IntegerField()
    timestamp=  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)


class StrainForm(forms.Form):
    strainkey = forms.IntegerField()
    timestamp=  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    gene = forms.CharField(max_length=20)
    genotype = forms.CharField(max_length=500)
    allele = forms.CharField(max_length=20)
    chromosome = forms.CharField(max_length=20)
    simulated = forms.CharField(max_length=1)


class TypeForm(forms.Form):
    typekey = forms.IntegerField()
    timestamp =  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)


"""
class UserForm(forms.Form):
    userid = forms.IntegerField()
    name = forms.CharField(max_length=20)
    accesslevel = forms.FloatField()
    labkey = MyModelChoiceField(queryset=Lab.objects.all())

"""

"""
class VideoattributesForm(forms.Form):
    videometadatakey = forms.CharField(, max_length=18)
    timestamp =  forms.DateTimeField()
    fps = forms.IntegerField()
    numframes = forms.FloatField()
    width = forms.IntegerField()
    height = forms.IntegerField()
    micronsperpixel = forms.IntegerField()

"""

class WormForm(forms.Form):
    wormkey = forms.IntegerField()
    timestamp=  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    strainkey = MyModelChoiceField(queryset=Strain.objects.all())
    sex = forms.CharField(max_length=20)
    thaweddate = forms.DateTimeField()
    generationssincethawing = forms.FloatField()
    habituation = forms.CharField(max_length=20)


class WormfeatureForm(forms.Form):
    wormfeaturekey = forms.IntegerField()
    typekey = MyModelChoiceField(queryset=Type.objects.all())
    categorykey = MyModelChoiceField(queryset=Category.objects.all())
    directionkey = MyModelChoiceField(queryset=Direction.objects.all())
    aspectkey = MyModelChoiceField(queryset=Aspect.objects.all())
    bodypartkey = MyModelChoiceField(queryset=Bodypart.objects.all())
    featureindex = forms.FloatField()
    timestamp =  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=20)
    shorttitle = forms.CharField(max_length=20)
    description = forms.CharField(max_length=500)
    bin_width = forms.IntegerField()
    is_signed = forms.CharField(max_length=1)
    is_time_series = forms.CharField(max_length=1)
    is_zero_bin = forms.IntegerField()
    units = forms.CharField(max_length=20)
    signed_field = forms.CharField(max_length=20)
    remove_partial_events = forms.CharField(max_length=1)
    make_zero_if_empty = forms.CharField(max_length=1)
    name = forms.CharField(max_length=100)


class WorminteractionForm(forms.Form):
    worminteractionkey = forms.CharField(max_length=18)
    platewireframevideokey = MyModelChoiceField(queryset=Platewireframevideo.objects.all())
    wormlistkey = MyModelChoiceField(queryset=Wormlist.objects.all())
    timestamp =  forms.DateTimeField()
    framebyframewormparticipation = forms.CharField(max_length=500)
    area = forms.CharField(max_length=500)
    interactiontype = forms.CharField(max_length=20)
    startframe = forms.FloatField()
    endframe = forms.FloatField()


class WormlistForm(forms.Form):
    wormlistkey = forms.IntegerField()
    wormkey = MyModelChoiceField(queryset=Worm.objects.all())
    timestamp =  forms.DateTimeField()
    name = forms.CharField(max_length=100)


class WormmeasurementForm(forms.Form):
    wormmeasurementskey = forms.IntegerField()
    timestamp=  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)


class WormwireframevideoForm(forms.Form):
    wormwireframekey = forms.IntegerField()
    platewireframevideokey = MyModelChoiceField(queryset=Platewireframevideo.objects.all())
    timestamp =  forms.DateTimeField()
    name = forms.CharField(max_length=100)
    wireframevideo = forms.CharField(max_length=500)
    droppedframeinfo = forms.CharField(max_length=500)
