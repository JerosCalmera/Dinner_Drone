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

@order_blueprint.route("/order_edit_entry/<id>")
def order_edit(id):
    order = OrdersHistory.query.get(id)
    items = Menu.query.all()
    return render_template("/order/order_edit.jinja", title="Edit Order", order = order, items = items)

@order_blueprint.route("/order_edit_entry/<id>/submit", methods = ["POST"])
def order_edit_submit(id):
    order = OrdersHistory.query.get(id)
    items = Menu.query.all()

    order.order_date = request.form ["order_date"]
    #     = request.form ["menu_item"]
    # db.session.commit()

    # order_history = OrdersHistory.query.all()

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
            

    order_history = OrdersHistory.query.all()

    return render_template("/order/orders.jinja", title="Order History", title_2="Order Added!", order_histories = order_history)

def order_edit(id):
    pass
    # 1. Get form data (e.g., order_date = request.form["order_date"])
    # 2. Get OrderHistory object by id
    # 3. Update each OrderHistory attribute (e.g., order_history.order_date = order_date)
    # 4. Get OrderItems by order_history_id and update the menu_items_id
    # 5. db.session.commit()


@order_blueprint.route("/order_delete_entry/<id>/delete")
def order_delete(id):
    db.session.query(OrderItems).filter(OrderItems.order_history_id==id).delete()
    db.session.query(OrdersHistory).filter(OrdersHistory.id==id).delete()
    db.session.commit()
    order_history = OrdersHistory.query.all()
    return render_template("/order/orders.jinja", title="Order History", title_2="Order Deleted!", order_histories = order_history)
