import pika
import json
import smtplib


def callback(ch, method, properties, body):
    data = json.loads(body)

    send_data = '[{}],{}:{}'.format(data['type'], data['code'], data['body'])

    print("Writing log")
    with open('log.txt','a') as f:
            f.write(send_data)

    ch.basic_ack(delivery_tag=method.delivery_tag)




if __name__ == "__main__":
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange="logs", exchange_type='fanout')

        result = channel.queue_declare(exclusive=True)

        queue_name = result.method.queue

        channel.queue_bind(exchange="logs", queue=queue_name)

        print('[*] starting worker with queue {}'.format(queue_name))

        channel.basic_consume(callback, queue=queue_name , no_ack=False)

        channel.start_consuming()
