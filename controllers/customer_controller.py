from flask import render_template, redirect, Blueprint, request
from app import db
from models import Customers, OrdersHistory, OrderItems, Menu

customer_blueprint = Blueprint("customer", __name__)

@customer_blueprint.route("/customer")
def customer_page():
    customers = Customers.query.all()
    return render_template("/customer/customers.jinja", title="Customer Information", customers=customers)

@customer_blueprint.route("/customer_add_entry")
def redirect_c():
    return render_template("/customer/customer_add.jinja", title="Add A Customer")

@customer_blueprint.route("/customer_add", methods=["POST"])
def customer_add():

    customer_name = request.form ["customer_name"]
    customer_phone = request.form ["customer_phone"]
    customer_address = request.form ["customer_address"]

    customer = Customers(name = customer_name, phone = customer_phone, address = customer_address)

    db.session.add(customer)
    db.session.commit()
    customers = Customers.query.all()
    return render_template("/customer/customers.jinja", title="Customer Details", title_2="Customer Details Added!", customers=customers)

@customer_blueprint.route("/customer_edit_entry/<id>")
def customer_edit(id):
    customer = Customers.query.get(id)

    return render_template("/customer/customer_edit.jinja", title="Customer Details", customers=customer)

@customer_blueprint.route("/customer_edit_entry/<id>/submit", methods=["POST"])
def customer_edit_submit(id):

    customer = Customers.query.get(id)

    customer.name = request.form ["customer_name"]
    customer.phone = request.form ["customer_phone"]
    customer.address = request.form ["customer_address"]

    db.session.commit()

    customer = Customers.query.all()
    return render_template("/customer/customers.jinja", title="Customer Details", title_2="Customer Details Updated!", customers=customer)

@customer_blueprint.route("/customer_delete_entry/<id>/delete")
def customer_delete(id):
    c_del = db.session.query(Customers).filter_by(id=id).first()
    db.session.delete(c_del)
    db.session.commit()

    customer = Customers.query.all()
    return render_template("/customer/customers.jinja", title="Customer Information", title_2="Customer Details Removed!", customers=customer)


