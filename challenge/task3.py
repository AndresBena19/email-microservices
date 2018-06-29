from kombu.common import Broadcast
from celery import Celery


app = Celery("working20", backend="amqp://guest:guest@localhost", broker="amqp://localhost")
app.conf.task_queues = (Broadcast('broadcast_tasks'),)

app.conf.task_routes = {
    'tasks.callback': {
        'queue': 'broadcast_tasks',
        'exchange': 'broadcast_tasks'
    }
}


@app.task()
def callback(x,y):
    return x +y
