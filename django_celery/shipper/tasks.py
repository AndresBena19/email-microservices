from celery import current_app
from .models import File_Upload
from django.contrib.auth.models import User

import pandas as pd

app = current_app


@app.task()
def getname(id):
    obj = File_Upload.objects.get(id=id)
    value = pd.read_excel(obj.upload.path)

    data = value.to_dict()

    for _ in range(3000):
        Userval = User.objects.create(id=data['id'][_],
                                      last_login=data['last_login'][_],
                                      is_superuser=data['is_superuser'][_],
                                      username=data['username'][_],
                                      first_name=data['first_name'][_],
                                      last_name=data['last_name'][_],
                                      email=data['email'][_],
                                      is_staff=data['is_staff'][_],
                                      is_active=data['is_active'][_],
                                      date_joined=data['date_joined'][_])
        Userval.save()
