from django.db import models

# Create your models here.

class FileStorage(models.Model):
    FileId = models.AutoField(primary_key=True)
    FileName = models.CharField(max_length=100)
    UpdateDate = models.DateField(auto_now=False, auto_now_add=True)