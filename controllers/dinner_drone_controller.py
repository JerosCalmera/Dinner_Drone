from flask import render_template, redirect, Blueprint, request
from app import db
from models import Customers, OrdersHistory, OrderItems, Menu

dinner_drone_blueprint = Blueprint("dinner", __name__)

@dinner_drone_blueprint.route("/")
def landing_page():
    return render_template("/index.jinja", title="Please select and option from the nav bar to continue")

@dinner_drone_blueprint.route("/order")
def order_page():
    return render_template("/index.jinja", title="Customer Order History")
