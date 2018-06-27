import pika
import json
import sys

if __name__ == "__main__":
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', exchange_type='fanout')



        channel.basic_publish(

            exchange="logs",
            routing_key="",
            body=json.dumps({'type':'Error',
                             'code':'12345',
                             'body': 'Server exploit'})
        )

        print("END")
