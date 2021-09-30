from django.conf.urls import url
from FileStorageApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^filestorage$', views.filestorageAPI),
    url(r'^filestorage/([0-9]+)$', views.filestorageAPI),

    url(r'^filestorage/UploadFile$', views.UploadFile),
    
    url(r'^filestorage/DeleteFile$', views.DeleteFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
