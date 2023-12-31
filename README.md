The following was the (to be the first of three) major solo project undertaken at CodeClan at week 5 (before the company went into liquidation), I created the website using SQL, SQLAlchemy, Python, Flask, Jinja2, and CSS.

# Dinner_Drone

The brief for the project was:
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Food Takeaway
You’ve been tasked with making an order management system for a takeaway. This takeaway takes orders over the phone and enters them into the system for the kitchen to cook them and to keep track of them.

MVP
You should be able to create an Order with a customer name, phone number, address, and a list of Items (an item should have a name and a price).

There should be a page where you can see all Orders and be able to click through to each Order to see the details where you should be able to edit or delete the Order.

Extensions:
Be able to order multiples of an item
Be able to add up total for an order
Be able to set an order as dispatched and delivered

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To run: create a SQL database named "dinner_drone" and init with flask, instructions below for SQLAlchemy to be entered into terminal in the dinner_drone root directory.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

createdb dinner_drone

flask init

flask migrate

flask upgrade

flask seed

flask run

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![screenshot](https://github.com/JerosCalmera/Dinner_Drone/assets/136751073/81b485e1-3a9f-492b-8704-17cce837b3d0)
