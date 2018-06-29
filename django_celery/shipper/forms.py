from django.forms import ModelForm
from .models import File_Upload
from .tasks import getname


class FileForm(ModelForm):
    class Meta:
        model = File_Upload
        fields = "__all__"

    def save(self, commit=True):
        value = super(FileForm, self).save(commit=False)
        value.save()
        getname.delay(value.id)
