from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from models import Strain, Worm
from serializers import StrainSerializer, WormSerializer
from django.http import HttpResponse
from django.http import Http404
from rest_framework import generics

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

class StrainListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Strain.objects.all()
    serializer_class = StrainSerializer

class StrainListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Strain.objects.all()
    serializer_class = StrainSerializer

class WormListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Worm.objects.all()
    serializer_class = WormSerializer


class WormListViewAll(generics.ListAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = Worm.objects.all()
    serializer_class = WormSerializer