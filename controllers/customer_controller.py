from flask import render_template, redirect, Blueprint, request
from app import db
from models import Customer, OrderHistory, OrderItem, Menu

customer_blueprint = Blueprint("customer", __name__)

@customer_blueprint.route("/customer")
def customer_page():
    customers = Customer.query.all()
    return render_template("/customers.jinja", title="Customer Information", customers=customers)

@customer_blueprint.route("/customer_add_entry")
def redirect_c():
    return render_template("/customer_add.jinja", title="Add A Customer item")

@customer_blueprint.route("/customer_add", methods=["POST"])
def customer_add():

    customer_name = request.form ["customer_name"]
    customer_phone = request.form ["customer_phone"]
    customer_address = request.form ["customer_address"]

    customer = Customer(name = customer_name, phone = customer_phone, address = customer_address)

    db.session.add(customer)
    db.session.commit()
    customers = Customer.query.all()
    return render_template("/customers.jinja", title="Customer Details", title_2="Customer Details Added!", customers=customers)

@customer_blueprint.route("/customer_delete_entry/<id>/delete")
def customer_delete(id):
    db.session.query(Customer).filter(Customer.id==id).delete()
    db.session.commit()
    customers = Customer.query.all()
    return render_template("/customers.jinja", title="Customer Information", title_2="Customer Details Removed!", customers=customers)


