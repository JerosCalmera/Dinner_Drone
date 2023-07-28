from flask import render_template, redirect, Blueprint, request
from app import db
# Import models

Dinner_Drone_blueprint = Blueprint("dinner", __name__)

# # Example of showing an individual object
# @example_blueprint.route("/example/<id>")
# def example_show(id):
#     example_obj = Example.query.get(id)
#     return render_template("example/show.html", example=example_obj)

@Dinner_Drone_blueprint.route("/")
def landing_page():
    return "Hello World"

@Dinner_Drone_blueprint.route("/order")
def order_page():
    return "Order page"

@Dinner_Drone_blueprint.route("/customer")
def customer_page():
    return "customer info page"

@Dinner_Drone_blueprint.route("/menu")
def menu_page():
    return "menu page"
