from rest_framework import serializers
from models import *
from django.contrib.auth.models import User

class MyPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def label_from_instance(self, obj):
        return "id: " + str(obj.id) + " name: "+ obj.name

class AspectSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Aspect
        fields = ('id', 'timestamp', 'name', 'description')

class BodypartSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Bodypart
        fields = ('id', 'timestamp', 'name', 'description', 'startskeletonindex', 'endskeletonindex', 'startskeletonindexdeprecated', 'endskeletonindexdeprecated')

class CategorySerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Category
        fields = ('id', 'timestamp', 'name', 'description')

class ComputervisionalgorithmSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Computervisionalgorithm
        fields = ('id', 'timestamp', 'name', 'description', 'framebyframe', 'author', 'academicpaper', 'code')

class DirectionSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Direction
        fields = ('id', 'timestamp', 'name', 'description')

class ExperimenterSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    labkey = MyPrimaryKeyRelatedField(queryset=Lab.objects.all())

    class Meta:
        model = Experimenter
        fields = ('id', 'timestamp', 'labkey', 'name', 'description')
        
class FeaturesperplatewireframeSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    platefeaturekey = MyPrimaryKeyRelatedField(queryset=Platefeature.objects.all())
    platewireframevideokey = MyPrimaryKeyRelatedField(queryset=Platewireframevideo.objects.all())

    class Meta:
        model = Featuresperplatewireframe
        fields = ('id', 'timestamp', 'platefeaturekey', 'platewireframevideokey', 'value')
        
class FeaturesperwormwireframeSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    wormfeaturekey = MyPrimaryKeyRelatedField(queryset=Wormfeature.objects.all())
    wormwireframekey = MyPrimaryKeyRelatedField(queryset=Wormwireframevideo.objects.all())

    class Meta:
        model = Featuresperwormwireframe
        fields = ('id', 'timestamp', 'wormfeaturekey', 'wormwireframekey', 'value')
        
class HistogramsperplatewireframeSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    platewireframevideokey = MyPrimaryKeyRelatedField(queryset=Platewireframevideo.objects.all())

    class Meta:
        model = Histogramsperplatewireframe
        fields = ('id', 'timestamp', 'platewireframevideokey', 'bins', 'counts')
        
class HistogramsperwormwireframeSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    eventdirectionkey = MyPrimaryKeyRelatedField(queryset=Direction.objects.all())
    wormfeaturekey = MyPrimaryKeyRelatedField(queryset=Wormfeature.objects.all())
    wormwireframekey = MyPrimaryKeyRelatedField(queryset=Wormwireframevideo.objects.all())
    signkey = MyPrimaryKeyRelatedField(queryset=Sign.objects.all())

    class Meta:
        model = Histogramsperwormwireframe
        fields = ('id', 'timestamp', 'eventdirectionkey', 'wormfeaturekey', 'wormwireframekey', 'signkey', 'bins', 'counts')
        
class LabSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Lab
        fields = ('id', 'timestamp', 'name', 'description', 'address')
        
class MeasurementsperwormwireframeSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    wormmeasurementkey = MyPrimaryKeyRelatedField(queryset=Wormmeasurement.objects.all())
    wormwireframekey = MyPrimaryKeyRelatedField(queryset=Wormwireframevideo.objects.all())

    class Meta:
        model = Measurementsperwormwireframe
        fields = ('id', 'timestamp', 'wormmeasurementkey', 'wormwireframekey', 'value')
        
class PlateSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    experimenterkey = MyPrimaryKeyRelatedField(queryset=Experimenter.objects.all())
    wormlistkey = MyPrimaryKeyRelatedField(queryset=Wormlist.objects.all())

    class Meta:
        model = Plate
        fields = ('id', 'name', 'timestamp', 'sampletype', 'startdatetime', 'copyright', 'vulvaorientation', 'annotation', 'chemicals', 'food', 'illumination', 'temperature', 'tracker', 'agarside', 'gasconcentration', 'experimenterkey', 'wormlistkey' )

class PlatefeatureSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Platefeature
        fields = ('id', 'timestamp', 'name', 'description', 'title', 'shorttitle')

class PlaterawvideoSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    platekey = MyPrimaryKeyRelatedField(queryset=Plate.objects.all())
    #videometadatakey = MyPrimaryKeyRelatedField(queryset=Videoattributes.objects.all())

    class Meta:
        model = Platerawvideo
        fields = ('id', 'timestamp', 'name', 'description', 'title', 'shorttitle', 'videofile', 'fps', 'numframes', 'width', 'height', 'micronsperpixel', 'platekey')
        
class PlatewireframevideoSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    platerawvideokey = MyPrimaryKeyRelatedField(queryset=Platerawvideo.objects.all())
    cvalgorithmkey = MyPrimaryKeyRelatedField(queryset=Computervisionalgorithm.objects.all())

    class Meta:
        model = Platewireframevideo
        fields = ('id', 'timestamp', 'platerawvideokey', 'cvalgorithmkey', 'wireframevideo', 'droppedframeinfo')
        
class SignSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Sign
        fields = ('id', 'timestamp', 'name', 'description')
        
class StrainSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Strain
        fields = ('id', 'timestamp', 'strain_name', 'gene', 'genotype', 'allele', 'chromosome', 'simulated')
        
class TypeSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Type
        fields = ('id', 'timestamp', 'name', 'description')

"""
class VideoattributesSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Videoattributes
        fields = ('id', 'timestamp', 'fps', 'numframes', 'width', 'height', 'micronsperpixel')
"""

class WormSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    strainkey = MyPrimaryKeyRelatedField(queryset=Strain.objects.all())

    class Meta:
        model = Worm
        fields = ('id', 'timestamp', 'strainkey', 'sex', 'thaweddate', 'generationssincethawing', 'habituation')
        
class WormfeatureSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    typekey = MyPrimaryKeyRelatedField(queryset=Type.objects.all())
    categorykey = MyPrimaryKeyRelatedField(queryset=Category.objects.all())
    directionkey = MyPrimaryKeyRelatedField(queryset=Direction.objects.all())
    aspectkey = MyPrimaryKeyRelatedField(queryset=Aspect.objects.all())
    bodypartkey = MyPrimaryKeyRelatedField(queryset=Bodypart.objects.all())

    class Meta:
        model = Wormfeature
        fields = ('id', 'timestamp', 'typekey', 'categorykey', 'aspectkey', 'bodypartkey', 'featureindex', 'title', 'shorttitle', 'description', 'bin_width', 'is_signed', 'is_time_series', 'is_zero_bin', 'units', 'signed_field', 'remove_partial_events', 'make_zero_if_empty', 'name')
        
class WorminteractionSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    platewireframevideokey = MyPrimaryKeyRelatedField(queryset=Platewireframevideo.objects.all())
    wormlistkey = MyPrimaryKeyRelatedField(queryset=Wormlist.objects.all())

    class Meta:
        model = Worminteraction
        fields = ('id', 'timestamp', 'platewireframevideokey', 'wormlistkey', 'framebyframewormparticipation', 'area', 'interationtype', 'startframe', 'endframe')
        
class WormlistSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    wormkey = MyPrimaryKeyRelatedField(queryset=Worm.objects.all())

    class Meta:
        model = Wormlist
        fields = ('id', 'timestamp', 'wormkey', 'wormlist_identifier')
        
class WormmeasurementSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Wormmeasurement
        fields = ('id', 'timestamp', 'name', 'description')
        
class WormwireframevideoSerializer(serializers.ModelSerializer):
    #owner = MyPrimaryKeyRelatedField(queryset=User.objects.all())
    platewireframevideokey = MyPrimaryKeyRelatedField(queryset=Platewireframevideo.objects.all())

    class Meta:
        model = Wormwireframevideo
        fields = ('id', 'timestamp', 'platewireframevideokey', 'wireframevideo', 'droppedframeinfo')
        
