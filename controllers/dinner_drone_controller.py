from flask import render_template, redirect, Blueprint, request
from app import db
from models import Customer, OrderHistory, OrderItem, Menu

dinner_drone_blueprint = Blueprint("dinner", __name__)

# # Example of showing an individual object
# @example_blueprint.route("/example/<id>")
# def example_show(id):
#     example_obj = Example.query.get(id)
#     return render_template("example/show.html", example=example_obj)

@dinner_drone_blueprint.route("/")
def landing_page():
    return render_template("/index.jinja", title="Please select and option from the nav bar to continue")

@dinner_drone_blueprint.route("/order")
def order_page():
    return render_template("/index.jinja", title="Customer Order History")
