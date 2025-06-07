import random
from faker import Faker
import json

# Initialize Faker for generating fake data
fake = Faker()

# List of subcategories (products)
subcategories = [
    "mens-clothing",
    "womens-clothing",
    "kids-clothing",
    "footwear",
    "bags-backpacks",
    "watches",
    "sunglasses",
    "hats-caps",
    "jewelry",
    "sportswear"
]

# Sellers for each subcategory (keeping the names realistic)
fashion_retailers = {
    "mens-clothing": [
        {"name": "Shoppers Stop", "amazon_seller_fashion_id": "amazon_seller_mens_clothing_1"},
        {"name": "Pantaloons", "amazon_seller_fashion_id": "amazon_seller_mens_clothing_2"},
        {"name": "Myntra", "amazon_seller_fashion_id": "amazon_seller_mens_clothing_3"},
        {"name": "Ajio", "amazon_seller_fashion_id": "amazon_seller_mens_clothing_4"},
        {"name": "Bata India", "amazon_seller_fashion_id": "amazon_seller_mens_clothing_5"}
    ],
    "womens-clothing": [
        {"name": "Fabindia", "amazon_seller_fashion_id": "amazon_seller_womens_clothing_1"},
        {"name": "Vero Moda", "amazon_seller_fashion_id": "amazon_seller_womens_clothing_2"},
        {"name": "Zara", "amazon_seller_fashion_id": "amazon_seller_womens_clothing_3"},
        {"name": "H&M", "amazon_seller_fashion_id": "amazon_seller_womens_clothing_4"},
        {"name": "Van Heusen", "amazon_seller_fashion_id": "amazon_seller_womens_clothing_5"}
    ],
    "kids-clothing": [
        {"name": "FirstCry", "amazon_seller_fashion_id": "amazon_seller_kids_clothing_1"},
        {"name": "Babyoye", "amazon_seller_fashion_id": "amazon_seller_kids_clothing_2"},
        {"name": "Hopscotch", "amazon_seller_fashion_id": "amazon_seller_kids_clothing_3"},
        {"name": "Mothercare", "amazon_seller_fashion_id": "amazon_seller_kids_clothing_4"},
        {"name": "Limeroad", "amazon_seller_fashion_id": "amazon_seller_kids_clothing_5"}
    ],
    "footwear": [
        {"name": "Red Tape", "amazon_seller_fashion_id": "amazon_seller_footwear_1"},
        {"name": "Metro Shoes", "amazon_seller_fashion_id": "amazon_seller_footwear_2"},
        {"name": "Woodland", "amazon_seller_fashion_id": "amazon_seller_footwear_3"},
        {"name": "Crocs", "amazon_seller_fashion_id": "amazon_seller_footwear_4"},
        {"name": "Puma", "amazon_seller_fashion_id": "amazon_seller_footwear_5"}
    ],
    "bags-backpacks": [
        {"name": "Wildcraft", "amazon_seller_fashion_id": "amazon_seller_bags_backpacks_1"},
        {"name": "American Tourister", "amazon_seller_fashion_id": "amazon_seller_bags_backpacks_2"},
        {"name": "Samsonite", "amazon_seller_fashion_id": "amazon_seller_bags_backpacks_3"},
        {"name": "Lavie", "amazon_seller_fashion_id": "amazon_seller_bags_backpacks_4"},
        {"name": "Baggit", "amazon_seller_fashion_id": "amazon_seller_bags_backpacks_5"}
    ],
    "watches": [
        {"name": "Titan", "amazon_seller_fashion_id": "amazon_seller_watches_1"},
        {"name": "Fossil", "amazon_seller_fashion_id": "amazon_seller_watches_2"},
        {"name": "Casio", "amazon_seller_fashion_id": "amazon_seller_watches_3"},
        {"name": "Seiko", "amazon_seller_fashion_id": "amazon_seller_watches_4"},
        {"name": "Rolex", "amazon_seller_fashion_id": "amazon_seller_watches_5"}
    ],
    "sunglasses": [
        {"name": "Ray-Ban", "amazon_seller_fashion_id": "amazon_seller_sunglasses_1"},
        {"name": "Oakley", "amazon_seller_fashion_id": "amazon_seller_sunglasses_2"},
        {"name": "Maui Jim", "amazon_seller_fashion_id": "amazon_seller_sunglasses_3"},
        {"name": "Fastrack", "amazon_seller_fashion_id": "amazon_seller_sunglasses_4"},
        {"name": "Police", "amazon_seller_fashion_id": "amazon_seller_sunglasses_5"}
    ],
    "hats-caps": [
        {"name": "New Era", "amazon_seller_fashion_id": "amazon_seller_hats_caps_1"},
        {"name": "Adidas", "amazon_seller_fashion_id": "amazon_seller_hats_caps_2"},
        {"name": "Nike", "amazon_seller_fashion_id": "amazon_seller_hats_caps_3"},
        {"name": "Reebok", "amazon_seller_fashion_id": "amazon_seller_hats_caps_4"},
        {"name": "Puma", "amazon_seller_fashion_id": "amazon_seller_hats_caps_5"}
    ],
    "jewelry": [
        {"name": "Tanishq", "amazon_seller_fashion_id": "amazon_seller_jewelry_1"},
        {"name": "Kalyan Jewellers", "amazon_seller_fashion_id": "amazon_seller_jewelry_2"},
        {"name": "Malabar Gold", "amazon_seller_fashion_id": "amazon_seller_jewelry_3"},
        {"name": "CaratLane", "amazon_seller_fashion_id": "amazon_seller_jewelry_4"},
        {"name": "Pendants", "amazon_seller_fashion_id": "amazon_seller_jewelry_5"}
    ],
    "sportswear": [
        {"name": "Decathlon", "amazon_seller_fashion_id": "amazon_seller_sportswear_1"},
        {"name": "Nike", "amazon_seller_fashion_id": "amazon_seller_sportswear_2"},
        {"name": "Adidas", "amazon_seller_fashion_id": "amazon_seller_sportswear_3"},
        {"name": "Puma", "amazon_seller_fashion_id": "amazon_seller_sportswear_4"},
        {"name": "Reebok", "amazon_seller_fashion_id": "amazon_seller_sportswear_5"}
    ]
}

# Function to generate seller and product data
def generate_seller_data(subcategory, seller_info, unique_product_counter):
    seller_data = []
    product_ids_used = set()  # Set to keep track of already used product IDs
    
    for seller in seller_info:
        seller_id = seller['amazon_seller_fashion_id']
        # Generate 10 unique product ids for this seller
        product_ids = []
        while len(product_ids) < 10:
            product_id = f"amazon_fashion_{subcategory}_{unique_product_counter}"
            if product_id not in product_ids_used:
                product_ids.append(product_id)
                product_ids_used.add(product_id)
                unique_product_counter += 1
        
        # Construct seller's data in required format
        seller_data.append({
            "seller_id": seller_id,
            "seller_name": seller['name'],
            "store_name": fake.company(),
            "contact_info": {
                "email": fake.email(),
                "phone": fake.phone_number(),
                "address": fake.address()
            },
            "performance_metrics": {
                "average_rating": f"{random.uniform(4, 5):.1f}",
                "total_orders": random.randint(1000, 5000),
                "cancellation_rate": f"{random.uniform(1, 5):.1f}%",
                "on_time_delivery_rate": f"{random.uniform(95, 100):.1f}%"
            },
            "sellsProducts": product_ids
        })
    return seller_data, unique_product_counter

# Final output dictionary
output_data = {}
unique_product_counter = 1

# For each subcategory, generate seller data
for subcategory, sellers in fashion_retailers.items():
    seller_data, unique_product_counter = generate_seller_data(subcategory, sellers, unique_product_counter)
    output_data[subcategory] = seller_data
    unique_product_counter = 1

# Print the output as a JSON formatted string
file_path = "./fake_fashion_sellers.json"
with open(file_path, 'w') as file:
    json.dump(output_data, file, indent=4)