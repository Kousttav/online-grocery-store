import json

# Full path to your JSON file
file_path = r"D:\innovation\Online Grocery Store\ecommerce-project\database\product.json"

# Step 1: Load existing data
with open(file_path, "r") as file:
    data = json.load(file)

# Extract all existing product names
existing_names = {product["name"].lower() for product in data["products"]}

# Step 2: Loop for adding products
while True:
    print("\nEnter new product details:")

    name = input("Name: ").strip()
    if name.lower() in existing_names:
        print("⚠️  A product with this name already exists. Please enter a different product.")
        continue  # Skip and prompt again

    # Continue collecting rest of the product details
    new_product = {
        "name": name,
        "price": float(input("Price: ")),
        "original_price": float(input("Original Price: ")),
        "discount": input("Discount (e.g., 10%): "),
        "description": input("Short Description: "),
        "long_description": input("Long Description: "),
        "image_url": input("Main Image URL: "),
        "additional_images": input("Additional Image URLs (comma-separated): ").split(","),
        "stock_quantity": int(input("Stock Quantity: ")),
        "category": input("Category: "),
        "brand": input("Brand: "),
        "rating": float(input("Rating (out of 5): ")),
        "review_count": int(input("Review Count: "))
    }

    # Clean up image URLs
    new_product["additional_images"] = [
        url.strip() for url in new_product["additional_images"] if url.strip()
    ]

    # Append the new product
    data["products"].append(new_product)
    existing_names.add(name.lower())  # Update name set to prevent duplicates in the same run

    # Ask if user wants to add another
    c = input("\nDo you want to add another product? (Y/N): ")
    if c.lower() != "y":
        break

# Step 3: Capitalize each product name
for product in data["products"]:
    product["name"] = product["name"].title()  # Capitalize each word

# Step 4: Write updated data back to JSON file
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)

print("\n✅ All new products added successfully to db.json!")
