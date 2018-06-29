from django.forms import ModelForm
from .models import File_Upload
from .tasks import set_users


class FileForm(ModelForm):
    class Meta:
        model = File_Upload
        fields = "__all__"

    def save(self, commit=True):
        value = super(FileForm, self).save(commit=False)
        value.save()
        set_users.delay(value.id)
