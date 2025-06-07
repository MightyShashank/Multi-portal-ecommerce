import random
from faker import Faker
import json

# Initialize Faker for generating fake data
fake = Faker()

# List of subcategories (products)
subcategories = [
    "smartphones",
    "laptops",
    "tablets",
    "smartwatches",
    "headphones",
    "cameras",
    "gaming-consoles",
    "drones",
    "power-banks",
    "smart-home"
]

# List of sellers
electronics_retailers = [
    {"name": "Boulanger", "flipkart_seller_electronics_id": "flipkart_seller_electronics_1"},
    {"name": "Best Buy", "flipkart_seller_electronics_id": "flipkart_seller_electronics_2"},
    {"name": "Fry's Electronics", "flipkart_seller_electronics_id": "flipkart_seller_electronics_3"},
    {"name": "Walmart Electronics", "flipkart_seller_electronics_id": "flipkart_seller_electronics_4"},
    {"name": "Currys", "flipkart_seller_electronics_id": "flipkart_seller_electronics_5"},
    {"name": "MediaMarkt", "flipkart_seller_electronics_id": "flipkart_seller_electronics_6"},
    {"name": "Fnac", "flipkart_seller_electronics_id": "flipkart_seller_electronics_7"},
    {"name": "PC World", "flipkart_seller_electronics_id": "flipkart_seller_electronics_8"},
    {"name": "Best Denki", "flipkart_seller_electronics_id": "flipkart_seller_electronics_9"},
    {"name": "Target Electronics", "flipkart_seller_electronics_id": "flipkart_seller_electronics_10"}
]

# Generate unique product IDs for each subcategory
product_ids = {subcategory: [f"flipkart_electronics_{subcategory}_{i}" for i in range(1, 51)] for subcategory in subcategories}

# Function to generate a seller API structure
def generate_seller_api_structure(seller, subcategories, product_ids):
    # Pick 5 unique products from each subcategory for this seller
    products = []
    for subcategory in subcategories:
        selected_products = random.sample(product_ids[subcategory], 5)  # Randomly select 5 products
        products.extend(selected_products)  # Add these products to the seller's list
        # Remove the selected products from the subcategory list to prevent duplication
        for product in selected_products:
            product_ids[subcategory].remove(product)

    return {
        "retailer_id": seller["flipkart_seller_electronics_id"],
        "retailer_name": seller["name"],
        "retailer_store_name": f"{seller['name']}'s Store",
        "contact_info": {
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address()
        },
        "performance_metrics": {
            "average_rating": round(random.uniform(3.5, 5.0), 1),
            "total_orders": random.randint(500, 5000),
            "cancellation_rate": f"{random.randint(1, 10)}%",
            "on_time_delivery_rate": f"{random.randint(90, 100)}%"
        },
        "sellsProducts": products
    }

# Generate the seller API structures for all sellers
sellers_api_structure = [generate_seller_api_structure(seller, subcategories, product_ids) for seller in electronics_retailers]

# Save the sellers data as a JSON file
file_path = "./fake_electronics_sellers.json"
with open(file_path, 'w') as file:
    json.dump(sellers_api_structure, file, indent=4)
