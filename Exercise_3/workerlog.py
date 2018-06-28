import pika
import json


def callback(ch, method, properties, body):
    data = json.loads(body)

    send_data = '[{}] {}:{}'.format(data['type'], data['code'], data['body'])

    print("Writing log")
    with open('log.txt','a') as f:
            f.write(send_data)






if __name__ == "__main__":

    status = ["Error","Info","Debug","Warning"]
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
        channel = connection.channel()
        channel.exchange_declare(exchange="logs", exchange_type='direct')

        result = channel.queue_declare(exclusive=True)

        queue_name = result.method.queue

        for type in status:
            channel.queue_bind(exchange="logs", queue=queue_name, routing_key=type)


        print('[*] starting worker with queue {}'.format(queue_name))

        channel.basic_consume(callback, queue=queue_name , no_ack=True)

        channel.start_consuming()
