from flask import Blueprint, render_template

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/cart')
def cart():
    return render_template('orders/cart.html')

@orders_bp.route('/checkout')
def checkout():
    return render_template('orders/checkout.html')

@orders_bp.route('/confirmation')
def confirmation():
    return render_template('orders/confirmation.html')
