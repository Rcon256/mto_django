
from rest_framework import status
from rest_framework.response import Response
from .models import News
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewsSerializer
    def delete(self, request, id=None):
        news = News.objects.filter(id=id)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, id=None):

        news = News.objects.filter(id=id)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)