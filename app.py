from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import all models

app = Flask(__name__)

# TODO: Fill in username/password and database_name
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:@localhost:5432/dinner_drone"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and Register Controllers
from models import Customer, OrderHistory, OrderItem, Menu

@app.route("/")
def home():
    return render_template("index.jinja", title="Hello World")

from seed import seed
app.cli.add_command(seed)