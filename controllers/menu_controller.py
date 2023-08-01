from flask import render_template, redirect, Blueprint, request
from app import db
from models import Customers, OrdersHistory, OrderItems, Menu

menu_blueprint = Blueprint("menu", __name__)

@menu_blueprint.route("/menu")
def menu_page():
    menu = Menu.query.all()
    return render_template("/menu/menu.jinja", title="Menu Items", menu=menu)

@menu_blueprint.route("/menu_add_item")
def redirect_m():
    return render_template("/menu/menu_add.jinja", title="Add A Menu item")

@menu_blueprint.route("/menu_add", methods=["POST"])
def menu_add():

    item_name = request.form ["item_name"]
    item_price = request.form ["item_price"]
    item_type = request.form ["item_type"]

    menu = Menu(item_name = item_name, item_type = item_type, item_price = item_price)

    db.session.add(menu)
    db.session.commit()
    add_menu = Menu.query.all()
    return render_template("/menu/menu.jinja", title="Menu Items", title_2="Item Added!", menu=add_menu)

@menu_blueprint.route("/menu_item_delete/<id>/delete")
def menu_delete(id):
    db.session.query(OrderItems).filter(OrderItems.menu_items_id==id).delete()
    db.session.query(Menu).filter(Menu.id==id).delete()
    db.session.commit()
    menu = Menu.query.all()
    return render_template("/menu/menu.jinja", title="Menu Items", title_2="Item Removed!", menu=menu)
