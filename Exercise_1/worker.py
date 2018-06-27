import pika
import json
import smtplib

def importers(ch, method, properties, body):
    data = json.loads(body)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ivanspoof@gmail.com', 'ghdqzh30db2')
    server.sendmail(data['from'], data['destine'], data['body'])
    server.quit()



if __name__ == "__main__":
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()
        channel.queue_declare(queue="importers")

        channel.basic_consume(importers,queue="importers", no_ack=True)
        print("WORKER START")
        channel.start_consuming()


