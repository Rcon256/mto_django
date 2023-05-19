
from rest_framework import status
from rest_framework.response import Response
from .models import Note
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import NoteSerializer
from rest_framework.decorators import action
from django.core import serializers
import json

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NoteSerializer
    def delete(self, request, id=None):
        note = Note.objects.filter(id=id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, id=None):

        note = Note.objects.filter(id=id)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @action(methods=['put'], detail=True)
    def setOk(self, request, *args, **kwargs):
        note = Note.objects.filter(id=self.kwargs['pk']).update(state=1)
        return Response(status=status.HTTP_200_OK)
    @action(methods=['put'], detail=True)
    def setBad(self, request, *args, **kwargs):
        note = Note.objects.filter(id=self.kwargs['pk']).update(state=0)
        return Response(status=status.HTTP_200_OK)
    @action(methods=['put'], detail=True)
    def setComment(self, request, *args, **kwargs):
        try:
            note = Note.objects.filter(id=self.kwargs['pk']).update(comment=request.data['comment'])
            return Response(status=status.HTTP_200_OK)
        except Exception as err:
            return Response(status.HTTP_304_NOT_MODIFIED)
        