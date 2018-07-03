from kombu import Exchange, Queue
from celery import Celery
from kombu import Consumer
from celery import bootsteps
import smtplib
import json

app = Celery("working20", backend="amqp://guest:guest@localhost", broker="amqp://localhost")
media_exchange = Exchange('broadcast_tasks', type='fanout')

app.conf.task_queues = (
    Queue(name='queue_task3', exchange=media_exchange, binding=media_exchange),
    Queue('email'),
)

app.conf.task_routes = {
    'tasks.sendmail': {
        'queue': 'email',
    }
}

@app.task(serializer='json')
def sendmail(data):
    send_data = '[{}] {} {}'.format(data['type'], data['code'], data['body'])
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ivanspoof@gmail.com', 'ghdqzh30db2')
    server.sendmail('ivanspoo@gmail.com', 'ivanspoof@gmail.com', send_data)
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
