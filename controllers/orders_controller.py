from flask import render_template, redirect, Blueprint, request
from app import db
from models.models import Customer, OrderHistory, OrderItem, Menu
from sqlalchemy.inspection import inspect

order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/orders")
def order_page():
    order_history = OrderHistory.query.order_by(OrderHistory.id.desc()).all()
    return render_template("/order/orders.jinja", title="Order History", order_histories = order_history)


@order_blueprint.route("/order_entry/<id>")
def order_details(id):
    order_history = OrderHistory.query.get(id)
    return render_template("/order/order_single.jinja", title="Single Order Info", order_histories = order_history)


@order_blueprint.route("/order_edit_entry/<id>")
def order_edit(id):
    order_history = OrderHistory.query.get(id)
    items = Menu.query.all()
    return render_template("/order/order_edit.jinja", title="Edit Order", items = items, order_histories = order_history)


@order_blueprint.route("/order_edit_entry/<id>/submit", methods = ["POST"])
def order_edit_submit(id):
    order_history = OrderHistory.query.get(id)
    items = Menu.query.all()

    order_history.order_notes = request.form ["order_notes"]
    db.session.commit()


    items = request.form.keys()
    for key in items:
        if key[0:5] == "item_":
            item_id_trim = key.split("_") # returns ["item", "item_id"]
            item_id = int(item_id_trim[1]) # list created, item is taken away, id remains 
            order_items_to_add = OrderItem(order_history_id = order_history.id, menu_items_id = item_id)
            db.session.add(order_items_to_add)
            db.session.commit()

    order_history = OrderHistory.query.order_by(OrderHistory.id.desc()).all()
    return render_template("/order/orders.jinja", title="Order History", title_2="Order Updated!", order_histories = order_history)


@order_blueprint.route("/order_edit_entry_date/<id>")
def order_edit_date(id):
    order_history = OrderHistory.query.get(id)
    items = Menu.query.all()
    return render_template("/order/order_edit_date.jinja", title="Edit Order", items = items, order_histories = order_history)

@order_blueprint.route("/order_edit_entry_date/<id>/submit", methods = ["POST"])
def order_edit_submit_date(id):
    order_history = OrderHistory.query.get(id)
    items = Menu.query.all()

    order_history.order_date = request.form ["order_date"]
    order_history.order_notes = request.form ["order_notes"]
    db.session.commit()

    items = request.form.keys()
    for key in items:
        if key[0:5] == "item_":
            item_id_trim = key.split("_") # returns ["item", "item_id"]
            item_id = int(item_id_trim[1]) # list created, item is taken away, id remains 
            order_items_to_add = OrderItem(order_history_id = order_history.id, menu_items_id = item_id)
            db.session.add(order_items_to_add)
            db.session.commit()

    order_history = OrderHistory.query.order_by(OrderHistory.id.desc()).all()
    return render_template("/order/orders.jinja", title="Order History", title_2="Order Updated!", order_histories = order_history)

@order_blueprint.route("/order_add_form")
def order_form():
    customers = Customer.query.all()
    items = Menu.query.all()
    return render_template("/order/order_add.jinja", title="Add An Order Entry Form", customers=customers, items=items)

@order_blueprint.route("/order_add", methods = ["POST"])
def order_form_s():
    customer_id = request.form ["customer_id"]
    order_date = request.form ["order_date"]
    order_notes = request.form ["order_notes"]

    order_history = OrderHistory(customer_id = customer_id, order_date = order_date, order_notes = order_notes)
    db.session.add(order_history)
    db.session.commit()

    items = request.form.keys()
    for key in items:
        if key[0:5] == "item_":
            item_id_trim = key.split("_") # returns ["item", "item_id"]
            item_id = int(item_id_trim[1]) # list created, item is taken away and left with id 
            order_items = OrderItem(order_history_id = order_history.id, menu_items_id = item_id)
            db.session.add(order_items)
            db.session.commit()

    order_history = OrderHistory.query.order_by(OrderHistory.id.desc()).all()

    return render_template("/order/orders.jinja", title="Order History", title_2="Order Added!", order_histories = order_history)

@order_blueprint.route("/order_delete_entry/<id>/delete")
def order_delete(id):
    o_del = db.session.query(OrderHistory).filter_by(id=id).first()
    db.session.delete(o_del)
    db.session.commit()

    order_history = OrderHistory.query.order_by(OrderHistory.id.desc()).all()
    return render_template("/order/orders.jinja", title="Order History", title_2="Order Deleted!", order_histories = order_history)

@order_blueprint.route("/order_delete_items/<id>/delete")
def order_delete_items(id):
    db.session.query(OrderItem).filter(OrderItem.order_history_id==id).delete()
    db.session.commit()
    order_history = OrderHistory.query.order_by(OrderHistory.id.desc()).all()
    return render_template("/order/orders.jinja", title="Order History", title_2="Order Items Cleared!", order_histories = order_history)
