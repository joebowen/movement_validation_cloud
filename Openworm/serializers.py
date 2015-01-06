from rest_framework import serializers
from models import *
from s3direct.widgets import S3DirectWidget
from django import forms
from django.contrib.auth.models import User

class AspectSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Aspect
        fields = ('id', 'timestamp', 'name', 'description')

class BodypartSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Bodypart
        fields = ('id', 'timestamp', 'name', 'description', 'startskeletonindex', 'endskeletonindex', 'startskeletonindexdeprecated', 'endskeletonindexdeprecated')

class CategorySerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Category
        fields = ('id', 'timestamp', 'name', 'description')

class ComputervisionalgorithmSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Computervisionalgorithm
        fields = ('id', 'timestamp', 'name', 'description', 'framebyframe', 'author', 'academicpaper', 'code')

class DirectionSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Direction
        fields = ('id', 'timestamp', 'name', 'description')

class ExperimenterSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    labkey = serializers.SlugRelatedField(queryset=Lab.objects.all(), slug_field='name')

    class Meta:
        model = Experimenter
        fields = ('id', 'timestamp', 'labkey', 'name', 'description')
        
class FeaturesperplatewireframeSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    platefeaturekey = serializers.SlugRelatedField(queryset=Platefeature.objects.all(), slug_field='name')
    platewireframevideokey = serializers.SlugRelatedField(queryset=Platewireframevideo.objects.all(), slug_field='name')

    class Meta:
        model = Featuresperplatewireframe
        fields = ('id', 'timestamp', 'platefeaturekey', 'platewireframevideokey', 'value')
        
class FeaturesperwormwireframeSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    wormfeaturekey = serializers.SlugRelatedField(queryset=Wormfeature.objects.all(), slug_field='name')
    wormwireframekey = serializers.SlugRelatedField(queryset=Wormwireframevideo.objects.all(), slug_field='name')

    class Meta:
        model = Featuresperwormwireframe
        fields = ('id', 'timestamp', 'wormfeaturekey', 'wormwireframekey', 'value')
        
class HistogramsperplatewireframeSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    platewireframevideokey = serializers.SlugRelatedField(queryset=Platewireframevideo.objects.all(), slug_field='name')

    class Meta:
        model = Histogramsperplatewireframe
        fields = ('id', 'timestamp', 'platewireframevideokey', 'bins', 'counts')
        
class HistogramsperwormwireframeSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    directionkey = serializers.SlugRelatedField(queryset=Direction.objects.all(), slug_field='name')
    wormfeaturekey = serializers.SlugRelatedField(queryset=Wormfeature.objects.all(), slug_field='name')
    wormwireframekey = serializers.SlugRelatedField(queryset=Wormwireframevideo.objects.all(), slug_field='name')
    signkey = serializers.SlugRelatedField(queryset=Sign.objects.all(), slug_field='name')

    class Meta:
        model = Histogramsperwormwireframe
        fields = ('id', 'timestamp', 'directionkey', 'wormfeaturekey', 'wormwireframekey', 'signkey', 'bins', 'counts')
        
class LabSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Lab
        fields = ('id', 'timestamp', 'name', 'description', 'address')
        
class MeasurementsperwormwireframeSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    wormmeasurementkey = serializers.SlugRelatedField(queryset=Wormmeasurement.objects.all(), slug_field='name')
    wormwireframekey = serializers.SlugRelatedField(queryset=Wormwireframevideo.objects.all(), slug_field='name')

    class Meta:
        model = Measurementsperwormwireframe
        fields = ('id', 'timestamp', 'wormmeasurementkey', 'wormwireframekey', 'value')
        
class PlateSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    experimenterkey = serializers.SlugRelatedField(queryset=Experimenter.objects.all(), slug_field='name')
    wormlistkey = serializers.SlugRelatedField(queryset=Wormlist.objects.all(), slug_field='name')

    class Meta:
        model = Plate
        fields = ('id', 'name', 'timestamp', 'sampletype', 'startdatetime', 'copyright', 'vulvaorientation', 'annotation', 'chemicals', 'food', 'illumination', 'temperature', 'tracker', 'agarside', 'gasconcentration', 'experimenterkey', 'wormlistkey' )

class PlatefeatureSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Platefeature
        fields = ('id', 'timestamp', 'name', 'description', 'title', 'shorttitle')

class PlaterawvideoSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    #platekey = serializers.SlugRelatedField(queryset=Plate.objects.all(), slug_field='name')
    platekey = serializers.SlugRelatedField(queryset=Plate.objects.all(), slug_field='name')

    class Meta:
        model = Platerawvideo
        fields = ('id', 'timestamp', 'name', 'description', 'title', 'shorttitle', 'videofileurl','fps', 'numframes', 'width', 'height', 'micronsperpixel', 'platekey')
        
class PlatewireframevideoSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    platerawvideokey = serializers.SlugRelatedField(queryset=Platerawvideo.objects.all(), slug_field='name')
    cvalgorithmkey = serializers.SlugRelatedField(queryset=Computervisionalgorithm.objects.all(), slug_field='name')

    class Meta:
        model = Platewireframevideo
        fields = ('id', 'timestamp', 'name', 'platerawvideokey', 'cvalgorithmkey', 'wireframevideo', 'droppedframeinfo')

class SignSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Sign
        fields = ('id', 'timestamp', 'name', 'description')
        
class StrainSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Strain
        fields = ('id', 'timestamp', 'name', 'gene', 'genotype', 'allele', 'chromosome', 'simulated')
        
class TypeSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Type
        fields = ('id', 'timestamp', 'name', 'description')

"""
class VideoattributesSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Videoattributes
        fields = ('id', 'timestamp', 'fps', 'numframes', 'width', 'height', 'micronsperpixel')
"""

class WormSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    strainkey = serializers.SlugRelatedField(queryset=Strain.objects.all(), slug_field='name')

    class Meta:
        model = Worm
        fields = ('id', 'timestamp', 'name', 'strainkey', 'sex', 'thaweddate', 'generationssincethawing', 'habituation')
        
class WormfeatureSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    typekey = serializers.SlugRelatedField(queryset=Type.objects.all(), slug_field='name')
    categorykey = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    directionkey = serializers.SlugRelatedField(queryset=Direction.objects.all(), slug_field='name')
    aspectkey = serializers.SlugRelatedField(queryset=Aspect.objects.all(), slug_field='name')
    bodypartkey = serializers.SlugRelatedField(queryset=Bodypart.objects.all(), slug_field='name')

    class Meta:
        model = Wormfeature
        fields = ('id', 'timestamp', 'name', 'typekey', 'categorykey', 'aspectkey', 'bodypartkey', 'featureindex', 'title', 'shorttitle', 'description', 'bin_width', 'is_signed', 'is_time_series', 'is_zero_bin', 'units', 'signed_field', 'remove_partial_events', 'make_zero_if_empty', 'name')
        
class WorminteractionSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    platewireframevideokey = serializers.SlugRelatedField(queryset=Platewireframevideo.objects.all(), slug_field='name')
    wormlistkey = serializers.SlugRelatedField(queryset=Wormlist.objects.all(), slug_field='name')

    class Meta:
        model = Worminteraction
        fields = ('id', 'timestamp', 'platewireframevideokey', 'wormlistkey', 'framebyframewormparticipation', 'area', 'interactiontype', 'startframe', 'endframe')
        
class WormlistSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    wormkey = serializers.SlugRelatedField(queryset=Worm.objects.all(), slug_field='name')

    class Meta:
        model = Wormlist
        fields = ('id', 'timestamp', 'name', 'wormkey')
        
class WormmeasurementSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Wormmeasurement
        fields = ('id', 'timestamp', 'name', 'description')
        
class WormwireframevideoSerializer(serializers.ModelSerializer):
    #owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    platewireframevideokey = serializers.SlugRelatedField(queryset=Platewireframevideo.objects.all(), slug_field='name')

    class Meta:
        model = Wormwireframevideo
        fields = ('id', 'timestamp', 'name', 'platewireframevideokey', 'wireframevideo', 'droppedframeinfo')
        
