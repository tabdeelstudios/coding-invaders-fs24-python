from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import NoteModel, BookModel
from .serializers import NoteSerializer, BookSerializer

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
        


class AllBooks(generics.GenericAPIView):
    # serializer_class=BookSerializer
    # queryset = BookModel.objects.all()

    def get(self, request):
        # notes = NoteModel.objects.all()
        # serializer = self.serializer_class(notes, many=True)
        return Response({
             "message":f"Fetching all books"
        })

class BookById(generics.GenericAPIView):
    # serializer_class=BookSerializer
    # queryset = BookModel.objects.all()

    def get(self, request, id):
    #     notes = BookModel.objects.all()
    #     serializer = self.serializer_class(notes, many=True)
        return Response({
            "message":f"Finding a book with ID : {id}"
        })