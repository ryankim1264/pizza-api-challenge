from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=4000)