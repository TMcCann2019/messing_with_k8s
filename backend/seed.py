from app import app, db
from models import Product

DATA = [
    {
        "name": "Tactical Shirt",
        "price": 25,
        "image": "https://example.com/1.jpg",
        "description": "Military style shirt"
    },
    {
        "name": "Operator Hoodie",
        "price": 40,
        "image": "https://example.com/2.jpg",
        "description": "Warm tactical hoodie"
    }
]

with app.app_context():
    db.drop_all()
    db.create_all()

    for item in DATA:
        db.session.add(Product(**item))

    db.session.commit()

    print("Seed complete")