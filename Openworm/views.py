from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from models import Openworm
from serializers import OpenwormSerializer
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

class OpenwormListView(APIView):
    queryset = Openworm.objects.all()

    def get(self, result, format=None):
        snippets = self.queryset
        serializer = OpenwormSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OpenwormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)