import pika
import json
import smtplib


def callback(ch, method, properties, body):
    data = json.loads(body)

    send_data = '[{}] {} {}'.format(data['type'], data['code'], data['body'])

    print('Sending email')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ivanspoof@gmail.com', 'ghdqzh30db2')
    server.sendmail('ivanspoo@gmail.com', 'ivanspoof@gmail.com', send_data)
    server.quit()




if __name__ == "__main__":
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange="logs", exchange_type='direct')

        result = channel.queue_declare(exclusive=True)

        queue_name = result.method.queue

        channel.queue_bind(exchange="logs", queue=queue_name, routing_key="Error")

        print('[*] starting worker with queue {}'.format(queue_name))

        channel.basic_consume(callback, queue=queue_name, no_ack=True)

        channel.start_consuming()
