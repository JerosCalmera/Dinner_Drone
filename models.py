from app import db
from datetime import datetime
# Example Model
# ------------------------------------------------
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))

class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(64))
    order_history = db.relationship('OrderHistory', backref='Customer')

    def __repr__(self):
        return f"<Customer: {self.id}: {self.name}: {self.address}>"

class OrderHistory(db.Model):
    __tablename__ = "order_history"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    order_date = db.Column(db.DateTime,default = datetime.utcnow)

class OrderItem(db.Model):
    __tablename__ = "order_item"
    id = db.Column(db.Integer, primary_key=True)
    order_history_id = db.Column(db.Integer, db.ForeignKey("order_history.id"))
    menu_items_id = db.Column(db.Integer, db.ForeignKey("menu.id"))

class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64))
    item_type = db.Column(db.String(64))
    item_price = db.Column(db.Integer)