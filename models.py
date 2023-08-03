from app import db
from datetime import datetime
from decimal import Decimal
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
    order_history = db.relationship('OrdersHistory', backref='customer', cascade='all, delete')

    def __repr__(self):
        return f"<Customer: {self.id}: {self.name}: {self.address}>"
    
    def get_total_spend(self):
        total_spend = 0
        for order_history in self.order_history:
            for order_item in order_history.order_items:
                total_spend += order_item.menu.item_price

        return total_spend

    def get_average_spend(self):
        average_list = []
        for order_history in self.order_history:
                average_list.append(order_history)
        
        average_s = "{:.2f}".format(len(average_list))

        total_spend = 0
        for order_history in self.order_history:
            for order_item in order_history.order_items:
                total_spend += order_item.menu.item_price

        if float(average_s) <= 0:
            return 0

        average_spend = float(total_spend) / float(average_s)
        return "{:.2f}".format(average_spend)
    
class OrdersHistory(db.Model):
    __tablename__ = "orders_history"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    order_date = db.Column(db.Date,default = datetime)
    order_notes = db.Column(db.String(64))
    order_items = db.relationship('OrderItems', backref="orders_history", cascade='all, delete')

    def calculate_total(self):
        order_total = 0
        for order_item in self.order_items:
            order_total += order_item.menu.item_price
        return order_total

    def delivery_fee(self):
        order_total_weight = 0
        delivery_fee = 5
        for order_item in self.order_items:
            order_total_weight += order_item.menu.item_weight

        if order_total_weight > 300:
            delivery_fee = 9.99
            if order_total_weight > 800:
                delivery_fee = 15.99
                if order_total_weight > 1500:
                    delivery_fee = 29.99
                    if order_total_weight > 2500:
                        delivery_fee = "----<b class=alert>Delivery Not Possible! Order over 2500g</b>----"
                        
        return delivery_fee

    def confirm_delivery(self, delivered):
        self.delivered = delivered

    def calculate_weight(self):
        order_total_weight = 0
        for order_item in self.order_items:
            order_total_weight += order_item.menu.item_weight
        return order_total_weight

    def calculate_g_total(self):
        order_total = 0
        order_total_weight = 0
        delivery_fee = 5

        for order_item in self.order_items:
            order_total += order_item.menu.item_price

        for order_item in self.order_items:
            order_total_weight += order_item.menu.item_weight

        if order_total_weight > 300:
            delivery_fee = 9.99
            if order_total_weight > 800:
                delivery_fee = 15.99
                if order_total_weight > 1500:
                    delivery_fee = 29.99


        order_total_d = order_total + Decimal(delivery_fee)
        return "{:.2f}".format(order_total_d)


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
    item_price = db.Column(db.Numeric(precision=9, scale=2))
    item_weight = db.Column(db.Numeric(precision=9, scale=0))
    order_items = db.relationship('OrderItems', backref="menu")
