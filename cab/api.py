from rest_framework import status
from rest_framework.response import Response
from .models import Cab
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CabSerializer

class CabViewSet(viewsets.ModelViewSet):
    queryset = Cab.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CabSerializer
    def delete(self, request, id=None):
        cabs = Cab.objects.filter(id=id)
        cabs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, id=None):

        cabs = Cab.objects.filter(id=id)
        serializer = CabSerializer(cabs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)