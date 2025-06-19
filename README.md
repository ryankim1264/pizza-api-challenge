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

## Create a virtual Enviroment

pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

---

## Configure Flask App

-export FLASK_APP=server/app.py

## Database Setup

- Initialize Migrations
       flask db init
- Generate Migration Script
       flask db migrate -m "Initial migration"
- Apply Migration
       flask db upgrade
---
## Seeding the Database
- Edit your server/seed.py with some initial data:
        python server/seed.py
- Running the App
        flask run
#### Server runs on: http://127.0.0.1:5000

---

| Method | Endpoint             | Description                               |
| ------ | -------------------- | ----------------------------------------- |
| GET    | `/restaurants`       | List all restaurants                      |
| GET    | `/restaurants/<id>`  | Get a single restaurant (with its pizzas) |
| DELETE | `/restaurants/<id>`  | Delete a restaurant                       |
| GET    | `/pizzas`            | List all pizzas                           |
| POST   | `/restaurant_pizzas` | Add a pizza to a restaurant               |

---

## Testing

-Prefered testing tool is postman

---

## Testing with Thunder Client

- Open Thunder Client (or Postman).
- Add requests for:GET /restaurants

GET /pizzas

POST /restaurant_pizzas

- URL: http://localhost:5000/restaurant_pizzas
- Body → JSON







 




