from kombu import Exchange, Queue
from celery import Celery
from kombu import Consumer
from celery import bootsteps


app = Celery("working10", backend="amqp://guest:guest@localhost", broker="amqp://localhost")
media_exchange = Exchange('broadcast_tasks', type='fanout')

app.conf.task_queues = (
    Queue(name='queue_task2', exchange=media_exchange, binding=media_exchange),

)


class MyConsumerStep(bootsteps.ConsumerStep):
    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[app.conf.task_queues[0]],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):

        send_data = '[{}] {}:{}'.format(body['type'], body['code'], body['body'])

        print("Writing log")
        with open('log.txt', 'a') as f:
            f.write(send_data)

        message.ack()


app.steps['consumer'].add(MyConsumerStep)
