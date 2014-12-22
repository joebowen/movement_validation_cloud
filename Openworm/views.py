from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from models import Openworm
from serializers import OpenwormSerializer
from django.http import StreamingHttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

class OpenwormListView(APIView):
    queryset = Openworm.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, result, format=None):
        snippets = self.queryset
        serializer = OpenwormSerializer(snippets, many=True)
        return StreamingHttpResponse(serializer.data)
        #return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        serializer = OpenwormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)