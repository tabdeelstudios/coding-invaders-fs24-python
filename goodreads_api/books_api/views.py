from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import NoteModel
from .serializers import NoteSerializer

# Create your views here.
class Note(generics.GenericAPIView):
    serializer_class=NoteSerializer
    queryset = NoteModel.objects.all()

    def get(self, request):
        notes = NoteModel.objects.all()
        serializer = self.serializer_class(notes, many=True)
        return Response({
            "notes":serializer.data
        })
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"SUCCESS", "data":{"note":serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"FAILED", "messages":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        