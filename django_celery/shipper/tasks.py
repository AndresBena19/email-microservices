from celery import current_app
from .models import File_Upload
from django.contrib.auth.models import User

import os
import sys
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import pandas as pd
from celery import chain

COMMASPACE = ', '
app = current_app


@app.task(serializer='json')
def set_users(_id):
    obj = File_Upload.objects.get(id=_id)
    values = pd.read_excel(obj.upload.path)

    data = values.to_dict()

    for _ in range(len(values)):
        if not User.objects.get(id=data['id'][_]):
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


@app.task()
def sendmail(path, _sender):
    sender = _sender
    gmail_password = 'ghdqzh30db2'
    recipients = ['ivanspoof@gmail.com']

    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'actives'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # List of attachments
    attachments = [path]

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise


@app.task(serializer='json')
def active_user():
    data = User.objects.filter(is_active=1)

    active_user = ['id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff',
                   'is_active']

    filter_data = []
    for _ in range(len(active_user)):
        value = map(lambda x: data[_].__dict__[x], active_user)
        filter_data.append(list(value))

    df = pd.DataFrame({column: value for column, value in zip(active_user, zip(*filter_data))})

    writer = pd.ExcelWriter('media/actives/actives.xlsx',datetime_format='dd/mm/yy', date_format='dd/mm/yy', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()

    return 'media/actives/actives.xlsx'


@app.task()
def dispacher():
    chain(active_user.si(), sendmail.s(_sender='ivanspoof@gmail.com'))()


@app.task()
def delete_active():
    pass
