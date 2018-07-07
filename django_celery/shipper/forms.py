from django.forms import ModelForm
from .models import File_Upload
from .tasks import set_users,active_user,sendmail
from celery import chain

class FileForm(ModelForm):
    class Meta:
        model = File_Upload
        fields = "__all__"

    def save(self, commit=True):
        value = super(FileForm, self).save(commit=False)
        value.save()

        chain(set_users.s(value.id), active_user.si(), sendmail.s(_sender='ivanspoof@gmail.com'))()

