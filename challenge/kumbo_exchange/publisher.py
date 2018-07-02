from kombu import Connection,Producer
from celery import Celery

app = Celery("working20", backend="amqp://guest:guest@localhost", broker="amqp://localhost")


def celery_message(value, producer=None):
    with app.producer_or_acquire(producer) as producer:
        producer.publish(
            body=value,
            serializer='json',
            exchange='broadcast_tasks'
        )

def kumbo_message(value):
    with Connection('amqp://guest:guest@localhost:5672//') as conn:
        with conn.channel() as channel:

            producer = Producer(channel)
            producer.publish(body=value,
                             exchange='broadcast_tasks',
                             serializer='json'
                                       )



if __name__ == "__main__":
   celery_message({'type':'Error',
                   'code':'12345',
                   'body': 'Server exploit'})
   """kumbo_message({'type':'Error',
                   'code':'12345',
                   'body': 'Server exploit'})"""

