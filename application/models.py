from .database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    role = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    requests = db.relationship("Requests", backref="user")


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(), nullable=False,default= "available")

    requests = db.relationship("Requests", backref="product")


class Requests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable = False)
    requests = db.Column(db.Integer, nullable=False, default=1)
    status = db.Column(db.String(), nullable=False, default="requested")



