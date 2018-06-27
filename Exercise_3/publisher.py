import pika
import json


if __name__ == "__main__":
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', exchange_type='direct')

        channel.basic_publish(

            exchange="logs",
            routing_key="Info",
            body=json.dumps({'type':'Debug',
                             'code':'12345',
                             'body': 'Server debugging'})
        )



        print("END")
