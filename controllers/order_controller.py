from flask import render_template, redirect, Blueprint, request
from app import db
from models import Customer, OrderHistory, OrderItem, Menu
from sqlalchemy.inspection import inspect

order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/orders")
def order_page():
    order_history = OrderHistory.query.all()
    return render_template("/orders.jinja", title="Order History", order_history = order_history)


@order_blueprint.route("/order_add_form")
def order_form():
    customers = Customer.query.all()
    items = Menu.query.all()
    return render_template("/order_add.jinja", title="Add An Order Entry Form", customers=customers, items=items)

@order_blueprint.route("/order_add", methods = ["POST"])
def order_form_s():
    customer_id = request.form ["customer_id"]
    date = request.form ["order_date"]

    orderhistory = OrderHistory(customer_id = customer_id, order_date = date)
    db.session.add(orderhistory)
    db.session.commit()

    item_id = request.form ["menu_item"]

    order = OrderItem(order_history_id = orderhistory.id, menu_items_id = item_id)

    db.session.add(order)
    db.session.commit()

    return render_template("/order_add.jinja", title="Order Added!")

# @order_blueprint.route("/order_add_sumbit", methods=["POST"])
# def order_form():
#     customer_name = request.form ["customer_name"]
