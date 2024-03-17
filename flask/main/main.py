from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
# set db constant: then set db connection = postgresql://user:password@host/table
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db/main"

# frontend set-up
CORS(app)

db = SQLAlchemy(app)


class Product(db.Model):
    # autoincrement=False -> product itself is created in Django app
    # this app is only catching the event from rabbitMQ -> it will create the product
    # don't want the id to be autoincrement, because the id will be different from django app
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint("user_id", "product_id", name="user_product_unique")


@app.route("/")
def index():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
