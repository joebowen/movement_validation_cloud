from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from models import Openworm
from serializers import OpenwormSerializer
from django.http import HttpResponse

class MyView(APIView):
    queryset = Openworm.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def index(self, request):
        return HttpResponse("Hello, world. You're at the poll index.")

    @api_view(['GET', 'POST'])
    def openworm_list(self, request):
        """
        List all snippets, or create a new snippet.
        """
        if request.method == 'GET':
            snippets = Openworm.objects.all()
            serializer = OpenwormSerializer(snippets, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = OpenwormSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'POST'])
    def openworm_detail(self, request):
        """
        List all snippets, or create a new snippet.
        """
        if request.method == 'GET':
            snippets = Openworm.objects.all()
            serializer = OpenwormSerializer(snippets, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = OpenwormSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)