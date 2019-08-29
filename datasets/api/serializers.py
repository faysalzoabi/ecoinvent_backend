from rest_framework import serializers
from datasets.models import DatasetData, DatasetFile, Version, System


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = "__all__"


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = "__all__"


class DatasetFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetFile
        fields = [
            'document',
            'uploaded_at',
            'version',
            'system'
            ]
   

class DatasetDataSerializer(serializers.ModelSerializer):
    datafile = DatasetFileSerializer()
    class Meta:
        model = DatasetData
        fields = [
            'activity_name',
            'geography',
            'referenceProductName',
            'datafile'
            ]
