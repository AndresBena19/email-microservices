from kombu.common import Broadcast
from celery import Celery
import smtplib

app = Celery("generator", backend="amqp://guest:guest@localhost", broker="amqp://localhost")
app.conf.task_queues = (Broadcast('broadcast_tasks'),)

@app.task()
def callback(x,y):
    return x +y

