from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from shipper import views

urlpatterns = [
    url(r'^file_upload/$', views.upload, name='UPLOAD_FILE'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)