import pika
import sys


msg = str(sys.argv[2])
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='job_queue')

channel.basic_publish(exchange='', routing_key='job_queue', body=bytes(msg, encoding='utf8'),
                      properties=pika.spec.BasicProperties(content_type='text', content_encoding='utf-8',
                                                           priority=1))


channel.basic_publish(exchange='', routing_key='job_queue', body=bytes(msg, encoding='utf8'),
                      properties=pika.spec.BasicProperties(content_type='text', content_encoding='utf-8',
                                                           priority=2))

channel.basic_publish(exchange='', routing_key='job_queue', body=bytes(msg, encoding='utf8'),
                      properties=pika.spec.BasicProperties(content_type='text', content_encoding='utf-8',
                                                           priority=3))
print(f" [x] Sent '{msg}'")
connection.close()
