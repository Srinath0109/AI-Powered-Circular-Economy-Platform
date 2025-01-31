from flask import Blueprint, request, jsonify
from models.db import db, Product
from services.recommendation import recommend_products

product_routes = Blueprint("products", __name__)

@product_routes.route("/", methods=["GET"])
def get_products():
    """Fetch all products"""
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@product_routes.route("/recommend", methods=["POST"])
def recommend():
    """AI-based recommendations"""
    user_preferences = request.json
    recommendations = recommend_products(user_preferences)
    return jsonify(recommendations)
