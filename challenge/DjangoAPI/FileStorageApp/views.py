import pdb
from django.http import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import parsers
from rest_framework.parsers import JSONParser
from django.http.response import FileResponse, JsonResponse

from FileStorageApp.models import FileStorage
from FileStorageApp.serializers import FileStorageSerializer

from django.core.files.storage import default_storage

import pathlib 
from pathlib import Path

import os

# Create your views here.

@csrf_exempt
def filestorageAPI(request, id=0):
    print(request)
    if request.method=='GET':
        files = FileStorage.objects.all()
        files_serializer = FileStorageSerializer(files, many=True)
        return JsonResponse(files_serializer.data, safe=False)
    elif request.method=='POST':
        files_data = JSONParser().parse(request)
        try:
            if not files_data['FilesName']:
                return JsonResponse("Please select files for upload", safe=False)
            for file in files_data["FilesName"]: #FilesName
                file_data = {"FileName":file}
                files_serializer = FileStorageSerializer(data=file_data)
                if files_serializer.is_valid():
                    files_serializer.save()
            return JsonResponse("Added Successfully.", safe=False)
        except ValueError as e:
            return JsonResponse("Failed to Add.", safe=False)
    elif request.method=='PUT':
        files_data = JSONParser().parse(request)
        files=FileStorage.objects.get(FileId=files_data['FileId'])
        files_serializer = FileStorageSerializer(files, data=files_data)
        if files_serializer.is_valid():
            files_serializer.save()
            return JsonResponse("Updated Successfully.", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method=='DELETE':
        files=FileStorage.objects.get(FileId=id)
        parent = pathlib.Path(__file__).parent.resolve()
        path = "%s/../media/%s"%(parent, files.FileName)
        if(Path(path).is_file()):
            os.remove(path)
        if files:
            files.delete()
        else:
            return JsonResponse("Error", safe=False)
        return JsonResponse("Deleted Success", safe=False)

@csrf_exempt
def UploadFile(request):
    files = request.FILES
    files_name = []
    for file in files.items():
        file_name = default_storage.save(file[1].name, file[1])
        files_name.append(file_name)
    return JsonResponse(files_name, safe=False)

@csrf_exempt
def DeleteFile(request):
    files = JSONParser().parse(request)
    parent = pathlib.Path(__file__).parent.resolve()
    if files["DeleteFileName"]:
        path = "%s/../media/%s"%(parent, files["DeleteFileName"])
        print(path)
        os.remove(path)
    return JsonResponse("Deleted Success", safe=False)
