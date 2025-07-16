import json
import os

# ✅ Absolute file path
PRODUCT_FILE = r"D:\innovation\Online Grocery Store\ecommerce-project\database\product.json"

def load_products():
    if not os.path.exists(PRODUCT_FILE):
        print("❌ Product file not found:", PRODUCT_FILE)
        return []

    with open(PRODUCT_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            products = data.get("products", [])

            # Assign IDs dynamically if not present
            for idx, product in enumerate(products):
                product.setdefault("id", idx)

            return products
        except json.JSONDecodeError as e:
            print("❌ JSON decode error:", e)
            return []


def get_product_by_id(product_id):
    products = load_products()
    for product in products:
        if product.get('id') == product_id:
            return product
    return None

if __name__ == "__main__":
    products = load_products()
    print(f"✅ Products loaded: {len(products)} items")
    # Optional: print sample data
    for p in products[:2]:
        print(f"- {p['name']} (${p['price']})")
