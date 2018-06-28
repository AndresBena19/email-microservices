from celery import Celery
from tasks import sendmail

if __name__=="__main__":
    value = sendmail.delay('ivanspoof@gmail.com', 'ivanspoof@gmail.com', "hola")

    result = value.ready()

    print(result)
