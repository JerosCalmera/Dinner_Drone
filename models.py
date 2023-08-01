from app import db
from datetime import datetime
# Example Model
# ------------------------------------------------
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))

class Customers(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    address = db.Column(db.String(64))
    order_history = db.relationship('OrdersHistory', backref='customer')

    def __repr__(self):
        return f"<Customer: {self.id}: {self.name}: {self.address}>"

class OrdersHistory(db.Model):
    __tablename__ = "orders_history"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    order_date = db.Column(db.Date,default = datetime)
    order_items = db.relationship('OrderItems', backref="orders_history")


class OrderItems(db.Model):
    __tablename__ = "order_items"
    id = db.Column(db.Integer, primary_key=True)
    order_history_id = db.Column(db.Integer, db.ForeignKey("orders_history.id"))
    menu_items_id = db.Column(db.Integer, db.ForeignKey("menu.id"))

class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64))
    item_type = db.Column(db.String(64))
    item_price = db.Column(db.Numeric(precision=9, scale=2), nullable=False)
    order_items = db.relationship('OrderItems', backref="menu")