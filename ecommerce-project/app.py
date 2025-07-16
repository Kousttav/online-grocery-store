from flask import Flask, render_template
from routes.auth import auth_bp
from routes.products import products_bp
from routes.orders import orders_bp
from models.product import load_products
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", os.urandom(16).hex())  # fallback

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(orders_bp, url_prefix='/orders')

    @app.route('/')
    def index():
        products = load_products()
        featured_product = products[:4]
        return render_template('index.html', featured_products=featured_product)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
