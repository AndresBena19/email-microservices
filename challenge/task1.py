from kombu.common import Broadcast
from celery import Celery
import smtplib

app = Celery("declarator", backend="amqp://guest:guest@localhost", broker="amqp://localhost")

app.conf.task_queues = (Broadcast('broadcast_tasks'),)
app.conf.task_routes = {
    'tasks.sendmail': {
        'queue': 'broadcast_tasks',
        'exchange': 'broadcast_tasks'
    }
}

@app.task()
def sendmail(x,y):
    return x +y

