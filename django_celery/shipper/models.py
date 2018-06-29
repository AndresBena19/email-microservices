from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class File_Upload(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='media/', validators = [FileExtensionValidator(allowed_extensions=['xls'])])

    def get_name(self):
        media, name = self.upload.name.split('/')
        return name

    def get_size(self):
        return '{0} bytes'.format(self.upload.size)


