from flask import render_template, redirect, Blueprint, request
from app import db
from models import Customer, OrderHistory, OrderItem, Menu

order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/order")
def order_page():
    order = OrderHistory.query.all()
    return render_template("/orders.jinja", title="Order History", order=order)

@order_blueprint.route("/order_add_entry")
def redirect_o():
    return render_template("/order_add.jinja", title="Add An Order Entry")

# @order_blueprint.route("/order_add", methods=["POST"])
# def order_add():

#     item_name = request.form ["item_name"]
#     item_price = request.form ["item_price"]
#     item_type = request.form ["item_type"]

#     order = order(item_name = item_name, item_type = item_type, item_price = item_price)

#     db.session.add(order)
#     db.session.commit()
#     add_order = order.query.all()
#     return render_template("/order.jinja", title="order Items", title_2="Item Added!", order=add_order)

# @order_blueprint.route("/order_item_delete/<id>/delete")
# def order_delete(id):
#     db.session.query(order).filter(order.id==id).delete()
#     db.session.commit()
#     order = order.query.all()
#     return render_template("/order.jinja", title="order Items", title_2="Item Removed!", order=order)
