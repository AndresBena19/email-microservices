from kombu.common import Broadcast
from celery import Celery

app = Celery("working2", backend="amqp://guest:guest@localhost", broker="amqp://localhost")
app.conf.task_queues = (Broadcast(name='broadcast_tasks'),)
