from django.shortcuts import render
from datasets.models import DatasetData, DatasetFile
from .serializers import DatasetDataSerializer, DatasetFileSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework	import	filters	
from django_filters	import	AllValuesFilter,DateTimeFilter,NumberFilter


class DataView(generics.ListAPIView):
     queryset = DatasetData.objects.all()
     serializer_class = DatasetDataSerializer

     filter_fields = (
        'activity_name',											
        'geography',
        )					
     search_fields = (
        '^activity_name',									
        )
     ordering_fields	=(	
        'activity_name',	
        )


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        files = DatasetFile.objects.all()
        serializer = DatasetFileSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        file_serializer = DatasetFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', file_serializer.errors)
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
   
            




