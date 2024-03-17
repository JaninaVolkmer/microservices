import pika, json

params = pika.URLParameters(
    "amqps://rxhycxqm:x13pYdQKi9vEOVoWuMFoT_3a2W0uLFOL@rat.rmq2.cloudamqp.com/rxhycxqm"
)

# create connection with RabbitMQ
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()

# publish
def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="", routing_key="admin", body=json.dumps(body), properties=properties
    )
