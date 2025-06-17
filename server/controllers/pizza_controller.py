from flask import Blueprint, jsonify
from server.models import Pizza

pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route('/', methods=['GET'])
def get_all_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict(rules=('-restaurant_pizzas',)) for p in pizzas]), 200
