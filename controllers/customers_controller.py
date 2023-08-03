from flask import render_template, redirect, Blueprint, request
from app import db
from models.models import Customer, OrderHistory, OrderItem, Menu

customer_blueprint = Blueprint("customer", __name__)

@customer_blueprint.route("/customer")
def customer_page():
    customers = Customer.query.all()
    return render_template("/customer/customers.jinja", title="Customer Details", customers=customers)

@customer_blueprint.route("/customer_add_entry")
def redirect_c():
    return render_template("/customer/customer_add.jinja", title="Add A Customer")

@customer_blueprint.route("/customer_add", methods=["POST"])
def customer_add():

    customer_name = request.form ["customer_name"]
    customer_phone = request.form ["customer_phone"]
    customer_address = request.form ["customer_address"]

    customer = Customer(name = customer_name, phone = customer_phone, address = customer_address)

    db.session.add(customer)
    db.session.commit()
    customers = Customer.query.all()
    return render_template("/customer/customers.jinja", title="Customer Details", title_2="Customer Details Added!", customers=customers)

@customer_blueprint.route("/customer_edit_entry/<id>")
def customer_edit(id):
    customer = Customer.query.get(id)

    return render_template("/customer/customer_edit.jinja", title="Customer Details", customers=customer)

@customer_blueprint.route("/customer_edit_entry/<id>/submit", methods=["POST"])
def customer_edit_submit(id):

    customer = Customer.query.get(id)

    customer.name = request.form ["customer_name"]
    customer.phone = request.form ["customer_phone"]
    customer.address = request.form ["customer_address"]

    db.session.commit()

    customer = Customer.query.all()
    return render_template("/customer/customers.jinja", title="Customer Details", title_2="Customer Details Updated!", customers=customer)

@customer_blueprint.route("/customer_delete_entry/<id>/delete")
def customer_delete(id):
    c_del = db.session.query(Customer).filter_by(id=id).first()
    db.session.delete(c_del)
    db.session.commit()

    customer = Customer.query.all()
    return render_template("/customer/customers.jinja", title="Customer Details", title_2="Customer Details Removed!", customers=customer)


