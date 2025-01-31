import numpy as np
import random
from models.db import Product

def recommend_products(user_preferences):
    """AI-based product recommendation system."""
    all_products = Product.query.all()
    if not all_products:
        return []

    # Dummy AI logic: Recommend random products from preferred category
    preferred_category = user_preferences.get("category", "")
    recommended = [p for p in all_products if p.category == preferred_category]

    if not recommended:
        recommended = random.sample(all_products, min(5, len(all_products)))

    return [p.to_dict() for p in recommended]
