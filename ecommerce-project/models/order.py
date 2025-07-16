import json
import os
from datetime import datetime

ORDER_FILE = os.path.join('database', 'orders.json')

def load_orders():
    if not os.path.exists(ORDER_FILE):
        return []
    with open(ORDER_FILE, 'r') as f:
        return json.load(f)

def save_orders(orders):
    with open(ORDER_FILE, 'w') as f:
        json.dump(orders, f, indent=2)

def create_order(user_id, product_id, quantity):
    orders = load_orders()
    new_order = {
        "id": max([o['id'] for o in orders], default=0) + 1,
        "user_id": user_id,
        "product_id": product_id,
        "quantity": quantity,
        "order_date": datetime.utcnow().isoformat()
    }
    orders.append(new_order)
    save_orders(orders)
    return new_order
