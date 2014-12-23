from rest_framework import serializers
from models import *
from django.contrib.auth.models import User

class StrainSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Strain
        fields = ('id', 'strain_name', 'timestamp', 'gene', 'genotype', 'allele', 'chromosome', 'simulated')

class WormSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    strainkey = serializers.PrimaryKeyRelatedField(queryset=Strain.objects.all())

    class Meta:
        model = Worm
        fields = ('id', 'timestamp', 'strainkey', 'sex', 'thaweddate', 'generationssincethawing','habituation')

class AspectSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Aspect
        fields = ('id', 'name', 'description')