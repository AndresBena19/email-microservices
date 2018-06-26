import pika
import json

if __name__ == "__main__":
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()
        channel.queue_declare(queue="importers")
        channel.basic_publish(

            exchange="",
            routing_key="importers",
            body=json.dumps({'from':'ivanspoof@gmail.com',
                             'destine':'ivanspoof@gmail.com',
                             'body': 'hi andres'})
        )

        print("END")
