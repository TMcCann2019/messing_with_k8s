from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db = SQLAlchemy(app)

from models import Product

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "image": p.image,
            "description": p.description
        }
        for p in products
    ])

@app.route("/products", methods=["POST"])
def create_product():
    data = request.json

    product = Product(
        name=data["name"],
        price=data["price"],
        image=data.get("image"),
        description=data.get("description")
    )

    db.session.add(product)
    db.session.commit()

    return {"message": "created"}, 201