#  Pizza API Challenge

A Flask API to manage restaurants, pizzas, and their relationships. Built with Flask, SQLAlchemy, Flask-Migrate.

---

##  Technologies Used

- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite (default DB)

---

Setup Instructions
1. Clone the repository:
bash
Copy
Edit
git clone 
cd pizza-api-challenge
2. Create a virtual environment using Pipenv:
bash
Copy
Edit
pipenv install
pipenv shell


Running the Application
bash
Copy
Edit
flask run
Ensure FLASK_APP=server/app.py is set if not already:

bash
Copy
Edit
export FLASK_APP=server/app.py

1. Initialize migrations:
bash
Copy
Edit
flask db init
2. Create migration script:
bash
Copy
Edit
flask db migrate -m "Initial migration"
3. Apply migration:
bash
Copy
Edit
flask db upgrade
4. Seed the database:
Create a seed.py file and run:

bash
Copy
Edit
python seed.py


Route Summary
Method	Endpoint	Description
GET	/restaurants	List all restaurants
GET	/restaurants/<id>	Get a single restaurant (with its pizzas)
DELETE	/restaurants/<id>	Delete a restaurant
GET	/pizzas	List all pizzas
POST	/restaurant_pizzas	Add a pizza to a restaurant

Use thunder client for these!



