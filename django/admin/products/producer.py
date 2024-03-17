# amqps://rxhycxqm:x13pYdQKi9vEOVoWuMFoT_3a2W0uLFOL@rat.rmq2.cloudamqp.com/rxhycxqm
import pika, json

params = pika.URLParameters(
    "amqps://rxhycxqm:x13pYdQKi9vEOVoWuMFoT_3a2W0uLFOL@rat.rmq2.cloudamqp.com/rxhycxqm"
)

# create connection with RabbitMQ
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()

# publish
# convert objects to json before send it
def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="", routing_key="main", body=json.dumps(body), properties=properties
    )
