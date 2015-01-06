from rest_framework import serializers
from models import *
from s3direct.widgets import S3DirectWidget
from django import forms
from django.contrib.auth.models import User

class AspectSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Aspect
        fields = ('id', 'timestamp', 'name', 'description')

class BodypartSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Bodypart
        fields = ('id', 'timestamp', 'name', 'description', 'startskeletonindex', 'endskeletonindex', 'startskeletonindexdeprecated', 'endskeletonindexdeprecated')

class CategorySerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Category
        fields = ('id', 'timestamp', 'name', 'description')

class ComputervisionalgorithmSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Computervisionalgorithm
        fields = ('id', 'timestamp', 'name', 'description', 'framebyframe', 'author', 'academicpaper', 'code')

class DirectionSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Direction
        fields = ('id', 'timestamp', 'name', 'description')

class ExperimenterSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    labkey = serializers.PrimaryKeyRelatedField(queryset=Lab.objects.all())

    class Meta:
        model = Experimenter
        fields = ('id', 'timestamp', 'labkey', 'name', 'description')
        
class FeaturesperplatewireframeSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    platefeaturekey = serializers.PrimaryKeyRelatedField(queryset=Platefeature.objects.all())
    platewireframevideokey = serializers.PrimaryKeyRelatedField(queryset=Platewireframevideo.objects.all())

    class Meta:
        model = Featuresperplatewireframe
        fields = ('id', 'timestamp', 'platefeaturekey', 'platewireframevideokey', 'value')
        
class FeaturesperwormwireframeSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    wormfeaturekey = serializers.PrimaryKeyRelatedField(queryset=Wormfeature.objects.all())
    wormwireframekey = serializers.PrimaryKeyRelatedField(queryset=Wormwireframevideo.objects.all())

    class Meta:
        model = Featuresperwormwireframe
        fields = ('id', 'timestamp', 'wormfeaturekey', 'wormwireframekey', 'value')
        
class HistogramsperplatewireframeSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    platewireframevideokey = serializers.PrimaryKeyRelatedField(queryset=Platewireframevideo.objects.all())

    class Meta:
        model = Histogramsperplatewireframe
        fields = ('id', 'timestamp', 'platewireframevideokey', 'bins', 'counts')
        
class HistogramsperwormwireframeSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    directionkey = serializers.PrimaryKeyRelatedField(queryset=Direction.objects.all())
    wormfeaturekey = serializers.PrimaryKeyRelatedField(queryset=Wormfeature.objects.all())
    wormwireframekey = serializers.PrimaryKeyRelatedField(queryset=Wormwireframevideo.objects.all())
    signkey = serializers.PrimaryKeyRelatedField(queryset=Sign.objects.all())

    class Meta:
        model = Histogramsperwormwireframe
        fields = ('id', 'timestamp', 'directionkey', 'wormfeaturekey', 'wormwireframekey', 'signkey', 'bins', 'counts')
        
class LabSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Lab
        fields = ('id', 'timestamp', 'name', 'description', 'address')
        
class MeasurementsperwormwireframeSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    wormmeasurementkey = serializers.PrimaryKeyRelatedField(queryset=Wormmeasurement.objects.all())
    wormwireframekey = serializers.PrimaryKeyRelatedField(queryset=Wormwireframevideo.objects.all())

    class Meta:
        model = Measurementsperwormwireframe
        fields = ('id', 'timestamp', 'wormmeasurementkey', 'wormwireframekey', 'value')
        
class PlateSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    experimenterkey = serializers.PrimaryKeyRelatedField(queryset=Experimenter.objects.all())
    wormlistkey = serializers.PrimaryKeyRelatedField(queryset=Wormlist.objects.all())

    class Meta:
        model = Plate
        fields = ('id', 'name', 'timestamp', 'sampletype', 'startdatetime', 'copyright', 'vulvaorientation', 'annotation', 'chemicals', 'food', 'illumination', 'temperature', 'tracker', 'agarside', 'gasconcentration', 'experimenterkey', 'wormlistkey' )

class PlatefeatureSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Platefeature
        fields = ('id', 'timestamp', 'name', 'description', 'title', 'shorttitle')

class PlaterawvideoSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    #platekey = serializers.PrimaryKeyRelatedField(queryset=Plate.objects.all())
    platekey = serializers.SlugRelatedField(queryset=Plate.objects.all(), many=False, slug_field='name')
    #videofile = forms.URLField(widget=S3DirectWidget(dest='destination_key_from_settings'))
    #videometadatakey = serializers.PrimaryKeyRelatedField(queryset=Videoattributes.objects.all())

    class Meta:
        model = Platerawvideo
        fields = ('id', 'timestamp', 'name', 'description', 'title', 'shorttitle', 'videofileurl','fps', 'numframes', 'width', 'height', 'micronsperpixel', 'platekey')
        
class PlatewireframevideoSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    platerawvideokey = serializers.PrimaryKeyRelatedField(queryset=Platerawvideo.objects.all())
    cvalgorithmkey = serializers.PrimaryKeyRelatedField(queryset=Computervisionalgorithm.objects.all())

    class Meta:
        model = Platewireframevideo
        fields = ('id', 'timestamp', 'name', 'platerawvideokey', 'cvalgorithmkey', 'wireframevideo', 'droppedframeinfo')

class SignSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Sign
        fields = ('id', 'timestamp', 'name', 'description')
        
class StrainSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Strain
        fields = ('id', 'timestamp', 'name', 'gene', 'genotype', 'allele', 'chromosome', 'simulated')
        
class TypeSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Type
        fields = ('id', 'timestamp', 'name', 'description')

"""
class VideoattributesSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Videoattributes
        fields = ('id', 'timestamp', 'fps', 'numframes', 'width', 'height', 'micronsperpixel')
"""

class WormSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    strainkey = serializers.PrimaryKeyRelatedField(queryset=Strain.objects.all())

    class Meta:
        model = Worm
        fields = ('id', 'timestamp', 'name', 'strainkey', 'sex', 'thaweddate', 'generationssincethawing', 'habituation')
        
class WormfeatureSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    typekey = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())
    categorykey = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    directionkey = serializers.PrimaryKeyRelatedField(queryset=Direction.objects.all())
    aspectkey = serializers.PrimaryKeyRelatedField(queryset=Aspect.objects.all())
    bodypartkey = serializers.PrimaryKeyRelatedField(queryset=Bodypart.objects.all())

    class Meta:
        model = Wormfeature
        fields = ('id', 'timestamp', 'name', 'typekey', 'categorykey', 'aspectkey', 'bodypartkey', 'featureindex', 'title', 'shorttitle', 'description', 'bin_width', 'is_signed', 'is_time_series', 'is_zero_bin', 'units', 'signed_field', 'remove_partial_events', 'make_zero_if_empty', 'name')
        
class WorminteractionSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    platewireframevideokey = serializers.PrimaryKeyRelatedField(queryset=Platewireframevideo.objects.all())
    wormlistkey = serializers.PrimaryKeyRelatedField(queryset=Wormlist.objects.all())

    class Meta:
        model = Worminteraction
        fields = ('id', 'timestamp', 'platewireframevideokey', 'wormlistkey', 'framebyframewormparticipation', 'area', 'interactiontype', 'startframe', 'endframe')
        
class WormlistSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    wormkey = serializers.PrimaryKeyRelatedField(queryset=Worm.objects.all())

    class Meta:
        model = Wormlist
        fields = ('id', 'timestamp', 'name', 'wormkey')
        
class WormmeasurementSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Wormmeasurement
        fields = ('id', 'timestamp', 'name', 'description')
        
class WormwireframevideoSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    platewireframevideokey = serializers.PrimaryKeyRelatedField(queryset=Platewireframevideo.objects.all())

    class Meta:
        model = Wormwireframevideo
        fields = ('id', 'timestamp', 'name', 'platewireframevideokey', 'wireframevideo', 'droppedframeinfo')
        
