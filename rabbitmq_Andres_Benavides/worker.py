import pika
import json
import smtplib

def importers(ch, method, properties, body):
    data = json.loads(body) 

    server = smtplib.SMTP('mail.smtp2go.com', 2525)
    server.login("pruebasspoofxxx@gmail.com", "emNia3J3ZHdxMmww")
    server.sendmail(data['from'], data['destine'], data['body'])


if __name__ == "__main__":
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()
        channel.queue_declare(queue="importers")

        channel.basic_consume(importers,queue="importers", no_ack=True)
        print("WORKER START")
        channel.start_consuming()


