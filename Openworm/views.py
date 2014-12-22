from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from models import Openworm
from serializers import OpenwormSerializer
from django.http import StreamingHttpResponse, HttpResponse
from rest_framework import generics
from django.http import Http404

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

class OpenwormListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return Openworm.objects.get(pk=pk)
        except Openworm.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippets = Openworm.objects.filter(pk=pk)
        serializer = OpenwormSerializer(snippets, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OpenwormSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk, format=None):
        serializer = OpenwormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)