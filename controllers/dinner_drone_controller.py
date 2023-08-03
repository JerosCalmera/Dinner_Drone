from flask import render_template, redirect, Blueprint, request
from app import db
from models.models import Customer, OrderHistory, OrderItem, Menu

dinner_drone_blueprint = Blueprint("dinner", __name__)

@dinner_drone_blueprint.route("/")
def landing_page():
    return render_template("/index.jinja", title="Login confirmed, Please select an option from the nav bar to continue")

@dinner_drone_blueprint.route("/info")
def order_page():
    return render_template("/info.jinja", title="Important Information")
