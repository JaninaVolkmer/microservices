import django

django.setup()
import pika, json
from products.models import Product


params = pika.URLParameters(
    "amqps://rxhycxqm:x13pYdQKi9vEOVoWuMFoT_3a2W0uLFOL@rat.rmq2.cloudamqp.com/rxhycxqm"
)

# create connection with RabbitMQ
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()

channel.queue_declare(queue="main")


def callback(channel, method, properties, body):
    print("Received in main")
    data = json.loads(body)
    print(data)

    if properties.headers["Content-Type"] == "product_created":
        # create product
        product = Product.objects.create(
            id=data["id"], title=data["title"], image=data["image"]
        )
        product.save()
        print("Product Created")

    elif properties.headers["Content-Type"] == "product_updated":
        product = Product.objects.get(data["id"])
        product.title = data["title"]
        product.image = data["image"]
        product.save()
        print("Product Updated")

    elif properties.headers["Content-Type"] == "product_deleted":
        product = Product.objects.get(data)
        product.delete()
        print("Product Deleted")


# auto_ack=True -> consume the calls, not get them again when container starts again
channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
