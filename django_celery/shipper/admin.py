from django.contrib import admin

# Register your models here.
from shipper.models import File_Upload


@admin.register(File_Upload)
class AdminFile(admin.ModelAdmin):
    list_display = ('id', 'get_name', 'get_size')
    ordering = ('id', )
