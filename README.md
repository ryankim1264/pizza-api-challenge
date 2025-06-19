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

2. Create and Activate Virtual Environment
Using pipenv:

bash
Copy
Edit
pipenv install
pipenv shell
Ensure pipenv is installed: pip install pipenv

3. Run Migrations
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade



