from rest_framework import serializers
from FileStorageApp.models import FileStorage

class FileStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileStorage
        fields = (
            'FileId',
            'FileName',
            'UpdateDate',
        )