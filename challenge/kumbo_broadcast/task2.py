from kombu.common import Broadcast
from celery import Celery
from kombu import Consumer, Queue
from celery import bootsteps
import smtplib

app = Celery("working2", backend="amqp://guest:guest@localhost", broker="amqp://localhost")
app.conf.task_queues = (Broadcast(name='broadcast_tasks'),
                        Queue('email'),)

app.conf.task_routes = {
    'tasks.sendmail': {
    'queue': 'email',
    }
}

@app.task
def sendmail(body):
    send_data = '[{}] {} {}'.format(body['type'], body['code'], body['body'])

    print('Sending email')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ivanspoof@gmail.com', 'ghdqzh30db2')
    server.sendmail('ivanspoo@gmail.com', 'ivanspoof@gmail.com', "hola")
    server.quit()


class MyConsumerStep(bootsteps.ConsumerStep):
    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[app.conf.task_queues[0]],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        if body['type'] == 'Error':
            print("call sendmail")
            sendmail.apply_async((body,),
                                 queue='email',
                                 exchange='',
                                 serializer='json')

            print("task called")
        message.ack()


app.steps['consumer'].add(MyConsumerStep)
