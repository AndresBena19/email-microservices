from kombu.common import Broadcast
from celery import Celery
from kombu import Consumer
from celery import bootsteps


app = Celery("working1", backend="amqp://guest:guest@localhost", broker="amqp://localhost")

app.conf.task_queues = (Broadcast(name='broadcast_tasks'),)


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
