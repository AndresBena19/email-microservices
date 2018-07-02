from kombu.common import Broadcast
from celery import Celery
from kombu import Consumer
from celery import bootsteps
import smtplib


app = Celery("working2", backend="amqp://guest:guest@localhost", broker="amqp://localhost")


app.conf.task_queues = (Broadcast(name='broadcast_tasks'),)


class MyConsumerStep(bootsteps.ConsumerStep):
    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[app.conf.task_queues[0]],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        send_data = '[{}] {} {}'.format(body['type'], body['code'], body['body'])

        if body['type'] == 'Error':
            print('Sending email')
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('ivanspoof@gmail.com', 'ghdqzh30db2')
            server.sendmail('ivanspoo@gmail.com', 'ivanspoof@gmail.com', send_data)
            server.quit()

        message.ack()


app.steps['consumer'].add(MyConsumerStep)
