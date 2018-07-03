from kombu.common import Broadcast
from celery import Celery
from kombu import Consumer, Queue
from celery import bootsteps

app = Celery("working2022", backend="amqp://guest:guest@localhost", broker="amqp://localhost")
app.conf.task_queues = (Broadcast(name='broadcast_tasks'),
                        Queue('logs'),)

app.conf.task_routes = {
    'tasks.write_log': {
     'queue': 'logs',
    }
}

@app.task()
def write_log(body):
    send_data = '[{}] {}:{}'.format(body['type'], body['code'], body['body'])

    print("Writing log")
    with open('log.txt', 'a') as f:
        f.write(send_data)


class MyConsumerStep(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[app.conf.task_queues[0]],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        write_log.apply_async((body,),
                              queue='logs',
                              exchange='')
        message.ack()


app.steps['consumer'].add(MyConsumerStep)
