import pika
import sys
import time


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='job_queue')

    def callback(ch, method, properties, body):
        print(ch, '...ch...', type(ch), '????', ch.__dict__)
        print(method, '...method...', type(method), '????', method.__dict__)
        print(properties, '...properties...', type(properties), '????', properties.__dict__)
        print(" [x] Received %r" % body)
        print('[x] Sleeping for 10 secs')
        time.sleep(10)

    channel.basic_consume(queue='job_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)

