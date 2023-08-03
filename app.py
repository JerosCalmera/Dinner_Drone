from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import all models

app = Flask(__name__)

# TODO: Fill in username/password and database_name
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:@localhost:5432/dinner_drone"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.models import Customer, OrderHistory, OrderItem, Menu

from controllers.dinner_drone_controller import dinner_drone_blueprint
from controllers.menu_controller import menu_blueprint
from controllers.customers_controller import customer_blueprint
from controllers.orders_controller import order_blueprint

app.register_blueprint(dinner_drone_blueprint)
app.register_blueprint(menu_blueprint)
app.register_blueprint(customer_blueprint)
app.register_blueprint(order_blueprint)

from seed import seed
app.cli.add_command(seed)