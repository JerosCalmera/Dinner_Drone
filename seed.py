from app import db
from models import Customer, OrderHistory, OrderItem, Menu
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Customer.query.delete()
    OrderHistory.query.delete()
    OrderItem.query.delete()
    Menu.query.delete()
    customer1 = Customer(name = "Jenny Wholesome", phone = "3452256234", address = "42 Arcadia Rd, Tadford")
    customer2 = Customer(name = "Elle Abbot", phone = "3428349123", address = "19 Belle Vue Rd, Colchester")
    customer3 = Customer(name = "Roberto Smith", phone = "1000667231", address = "742 Evergreen Terrace, Springton-On-Sea")
    customer4 = Customer(name = "Danny Almond", phone = "9982394157", address = "4 Crouch Lane, London")
    
    menu_item_1 = Menu(item_name = "None", item_type = "None" , item_price = 0.00)
    menu_item_2 = Menu(item_name = "Salad", item_type = "Starter" , item_price = 4.99)
    menu_item_3 = Menu(item_name = "Beef Stew", item_type = "Main", item_price = 9.99)
    menu_item_4 = Menu(item_name = "Lemon Sorbet", item_type = "Dessert" , item_price = 5.99)
    menu_item_5 = Menu(item_name = "Cola", item_type = "Drink", item_price = 0.99)

    db.session.add(customer1)
    db.session.add(customer2)
    db.session.add(customer3)
    db.session.add(customer4)

    db.session.add(menu_item_1)
    db.session.add(menu_item_2)
    db.session.add(menu_item_3)
    db.session.add(menu_item_4)
    db.session.add(menu_item_5)

    db.session.commit()