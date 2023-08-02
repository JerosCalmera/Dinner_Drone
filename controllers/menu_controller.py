from flask import render_template, redirect, Blueprint, request
from app import db
from models import Customers, OrdersHistory, OrderItems, Menu

menu_blueprint = Blueprint("menu", __name__)

@menu_blueprint.route("/menu")
def menu_page():
    menu = Menu.query.order_by(Menu.id.desc()).all()
    return render_template("/menu/menu.jinja", title="Menu Items", menu = menu)

@menu_blueprint.route("/menu_add_item")
def redirect_m():
    return render_template("/menu/menu_add.jinja", title="Add A Menu item")

@menu_blueprint.route("/menu_edit_entry/<id>")
def menu_edit(id):
    menu = Menu.query.get(id)
    return render_template("/menu/menu_edit.jinja", title="Menu Item", menu = menu)

@menu_blueprint.route("/menu_edit_entry/<id>/submit", methods=["POST"])
def menu_edit_submit(id):

    menu = Menu.query.get(id)

    menu.item_name = request.form ["item_name"]
    menu.item_type = request.form ["item_type"]
    menu.item_price = request.form ["item_price"]
    menu.item_weight = request.form ["item_weight"]

    db.session.commit()

    menu = Menu.query.order_by(Menu.id.desc()).all()
    return render_template("/menu/menu.jinja", title="Menu Items", title_2="Menu Item Updated!", menu = menu)

@menu_blueprint.route("/menu_add", methods=["POST"])
def menu_add():

    item_name = request.form ["item_name"]
    item_price = request.form ["item_price"]
    item_type = request.form ["item_type"]
    item_weight = request.form ["item_weight"]


    add_menu = Menu(item_name = item_name, item_type = item_type, item_price = item_price, item_weight = item_weight)

    db.session.add(add_menu)
    db.session.commit()

    menu = Menu.query.order_by(Menu.id.desc()).all()
    return render_template("/menu/menu.jinja", title="Menu Items", title_2="Item Added!", menu = menu)

@menu_blueprint.route("/menu_item_delete/<id>/delete")
def menu_delete(id):
    db.session.query(OrderItems).filter(OrderItems.menu_items_id==id).delete()
    db.session.query(Menu).filter(Menu.id==id).delete()
    db.session.commit()

    menu = Menu.query.order_by(Menu.id.desc()).all()
    return render_template("/menu/menu.jinja", title="Menu Items", title_2="Item Removed!", menu = menu)
