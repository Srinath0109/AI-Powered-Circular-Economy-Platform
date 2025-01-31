from flask import Flask
from routes.products import product_routes
from routes.users import user_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Register routes
app.register_blueprint(product_routes, url_prefix="/products")
app.register_blueprint(user_routes, url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True)
