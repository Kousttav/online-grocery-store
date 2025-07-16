from flask import Blueprint, render_template
from models.product import load_products, get_product_by_id

products_bp = Blueprint('products', __name__)

@products_bp.route('/')
def list_products():
    return render_template('products/list.html', products=load_products())

@products_bp.route('/<int:product_id>')
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return "Product not found", 404
    return render_template('products/detail.html', product=product)