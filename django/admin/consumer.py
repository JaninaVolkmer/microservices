import pika

params = pika.URLParameters(
    "amqps://rxhycxqm:x13pYdQKi9vEOVoWuMFoT_3a2W0uLFOL@rat.rmq2.cloudamqp.com/rxhycxqm"
)

# create connection with RabbitMQ
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(channel, method, properties, body):
    print("Received in admin")
    print(body)


# auto_ack=True -> consume the calls, not get them again when container starts again
channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
