from flask import render_template, redirect, Blueprint, request
from app import db
from models import Customers, OrdersHistory, OrderItems, Menu
from sqlalchemy.inspection import inspect

order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/orders")
def order_page():
    order_history = OrdersHistory.query.order_by(OrdersHistory.id.desc()).all()
    return render_template("/order/orders.jinja", title="Order History", order_histories = order_history)


@order_blueprint.route("/order_entry/<id>")
def order_details(id):
    order_history = OrdersHistory.query.get(id)

    order_total = 0
    for order_item in order_history.order_items:
        order_total += order_item.menu.item_price

    order_total_weight = 0
    for order_item in order_history.order_items:
        order_total_weight += order_item.menu.item_weight

    delivery_fee = 5
    order_total_d = order_total + delivery_fee

    if order_total_weight > 300:
        delivery_fee = 9.99
        if order_total_weight > 800:
            delivery_fee = 15.99
            if order_total_weight > 1500:
                delivery_fee = 29.99
                if order_total_weight > 2500:
                    order_total_weight = "Delivery Not Possible! Order over 2500"

    return render_template("/order/order_single.jinja", title="Single Order Info", order = order_history, order_total = order_total, order_total_weight = order_total_weight, order_total_d = order_total_d, delivery_fee = delivery_fee)



@order_blueprint.route("/order_edit_entry/<id>")
def order_edit(id):
    order_history = OrdersHistory.query.get(id)
    items = Menu.query.all()

    order_total = 0
    for order_item in order_history.order_items:
        order_total += order_item.menu.item_price

    order_total_weight = 0
    for order_item in order_history.order_items:
        order_total_weight += order_item.menu.item_weight

    delivery_fee = 5
    order_total_d = order_total + delivery_fee

    if order_total_weight > 300:
        delivery_fee = 9.99
        if order_total_weight > 800:
            delivery_fee = 15.99
            if order_total_weight > 1500:
                delivery_fee = 29.99
                if order_total_weight > 2500:
                    order_total_weight = "Delivery Not Possible! Order over 2500"

    return render_template("/order/order_edit.jinja", title="Edit Order", items = items, order = order_history, order_total = order_total, order_total_weight = order_total_weight, order_total_d = order_total_d, delivery_fee = delivery_fee)


@order_blueprint.route("/order_edit_entry/<id>/submit", methods = ["POST"])
def order_edit_submit(id):
    order_history = OrdersHistory.query.get(id)
    order_items = OrderItems.query.get(id)
    items = Menu.query.all()

    db.session.query(OrderItems).filter(OrderItems.order_history_id==id).delete()

    items = request.form.keys()
    for key in items:
        if key[0:5] == "item_":
            item_id_trim = key.split("_") # returns ["item", "item_id"]
            item_id = int(item_id_trim[1]) # list created, item is taken away, id remains 
            order_items_to_add = OrderItems(order_history_id = order_history.id, menu_items_id = item_id)
            db.session.add(order_items_to_add)
            db.session.commit()

    order_history = OrdersHistory.query.order_by(OrdersHistory.id.desc()).all()
    return render_template("/order/orders.jinja", title="Order History", title_2="Order Updated!", order_histories = order_history)


@order_blueprint.route("/order_edit_entry_date/<id>")
def order_edit_date(id):
    order_history = OrdersHistory.query.get(id)
    items = Menu.query.all()

    order_total = 0
    for order_item in order_history.order_items:
        order_total += order_item.menu.item_price

    order_total_weight = 0
    for order_item in order_history.order_items:
        order_total_weight += order_item.menu.item_weight

    delivery_fee = 5
    order_total_d = order_total + delivery_fee

    if order_total_weight > 300:
        delivery_fee = 9.99
        if order_total_weight > 800:
            delivery_fee = 15.99
            if order_total_weight > 1500:
                delivery_fee = 29.99
                if order_total_weight > 2500:
                    order_total_weight = "Delivery Not Possible! Order over 2500"

    return render_template("/order/order_edit_date.jinja", title="Edit Order", items = items, order = order_history, order_total = order_total, order_total_weight = order_total_weight, order_total_d = order_total_d, delivery_fee = delivery_fee)

@order_blueprint.route("/order_edit_entry_date/<id>/submit", methods = ["POST"])
def order_edit_submit_date(id):
    order_history = OrdersHistory.query.get(id)
    order_items = OrderItems.query.get(id)
    items = Menu.query.all()

    order_history.order_date = request.form ["order_date"]
    db.session.commit()
    db.session.query(OrderItems).filter(OrderItems.order_history_id==id).delete()

    items = request.form.keys()
    for key in items:
        if key[0:5] == "item_":
            item_id_trim = key.split("_") # returns ["item", "item_id"]
            item_id = int(item_id_trim[1]) # list created, item is taken away, id remains 
            order_items_to_add = OrderItems(order_history_id = order_history.id, menu_items_id = item_id)
            db.session.add(order_items_to_add)
            db.session.commit()

    order_history = OrdersHistory.query.order_by(OrdersHistory.id.desc()).all()
    return render_template("/order/orders.jinja", title="Order History", title_2="Order Updated!", order_histories = order_history)

@order_blueprint.route("/order_add_form")
def order_form():
    customers = Customers.query.all()
    items = Menu.query.all()
    
    return render_template("/order/order_add.jinja", title="Add An Order Entry Form", customers=customers, items=items)

@order_blueprint.route("/order_add", methods = ["POST"])
def order_form_s():
    customer_id = request.form ["customer_id"]
    date = request.form ["order_date"]

    order_history = OrdersHistory(customer_id = customer_id, order_date = date)
    db.session.add(order_history)
    db.session.commit()

    items = request.form.keys()
    for key in items:
        if key[0:5] == "item_":
            item_id_trim = key.split("_") # returns ["item", "item_id"]
            item_id = int(item_id_trim[1]) # list created, item is taken away and left with id 
            order_items = OrderItems(order_history_id = order_history.id, menu_items_id = item_id)
            db.session.add(order_items)
            db.session.commit()
            
    order_history = OrdersHistory.query.order_by(OrdersHistory.id.desc()).all()

    return render_template("/order/orders.jinja", title="Order History", title_2="Order Added!", order_histories = order_history)

@order_blueprint.route("/order_delete_entry/<id>/delete")
def order_delete(id):
    db.session.query(OrderItems).filter(OrderItems.order_history_id==id).delete()
    db.session.query(OrdersHistory).filter(OrdersHistory.id==id).delete()
    db.session.commit()
    order_history = OrdersHistory.query.order_by(OrdersHistory.id.desc()).all()
    return render_template("/order/orders.jinja", title="Order History", title_2="Order Deleted!", order_histories = order_history)
