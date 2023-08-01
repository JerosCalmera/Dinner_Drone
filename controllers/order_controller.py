from flask import render_template, redirect, Blueprint, request
from app import db
from models import Customers, OrdersHistory, OrderItems, Menu
from sqlalchemy.inspection import inspect

order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/orders")
def order_page():
    order_history = OrdersHistory.query.all()
    return render_template("/order/orders.jinja", title="Order History", order_histories = order_history)


@order_blueprint.route("/order_entry/<id>")
def order_details(id):
    order = OrdersHistory.query.get(id)
    return render_template("/order/order_single.jinja", title="Single Order Info", order = order)


@order_blueprint.route("/order_add_form")
def order_form():
    customers = Customers.query.all()
    items = Menu.query.all()
    return render_template("/order/order_add.jinja", title="Add An Order Entry Form", customers=customers, items=items)

@order_blueprint.route("/order_add", methods = ["POST"])
def order_form_s():
    customer_id = request.form ["customer_id"]
    date = request.form ["order_date"]

    orderhistory = OrdersHistory(customer_id = customer_id, order_date = date)
    db.session.add(orderhistory)
    db.session.commit()

    item_id = request.form ["menu_item"]
    order = OrderItems(order_history_id = orderhistory.id, menu_items_id = item_id)

    db.session.add(order)
    db.session.commit()
    order_history = OrdersHistory.query.all()
    return render_template("/order/orders.jinja", title="Order History", title_2="Order Added!", order_histories = order_history)


@order_blueprint.route("/order_delete_entry/<id>/delete")
def order_delete(id):
    db.session.query(OrderItems).filter(OrderItems.order_history_id==id).delete()
    db.session.query(OrdersHistory).filter(OrdersHistory.id==id).delete()
    db.session.commit()
    order_history = OrdersHistory.query.all()
    return render_template("/order/orders.jinja", title="Order History", title_2="Order Deleted!", order_histories = order_history)
