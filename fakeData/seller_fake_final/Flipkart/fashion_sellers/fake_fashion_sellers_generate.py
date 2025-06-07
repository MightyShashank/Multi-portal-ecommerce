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
        {"name": "H&M", "flipkart_seller_fashion_id": "flipkart_seller_mens_clothing_1"},
        {"name": "Zara", "flipkart_seller_fashion_id": "flipkart_seller_mens_clothing_2"},
        {"name": "Myntra", "flipkart_seller_fashion_id": "flipkart_seller_mens_clothing_3"},
        {"name": "AJIO", "flipkart_seller_fashion_id": "flipkart_seller_mens_clothing_4"},
        {"name": "Levi's", "flipkart_seller_fashion_id": "flipkart_seller_mens_clothing_5"}
    ],
    "womens-clothing": [
        {"name": "Biba", "flipkart_seller_fashion_id": "flipkart_seller_womens_clothing_1"},
        {"name": "Vero Moda", "flipkart_seller_fashion_id": "flipkart_seller_womens_clothing_2"},
        {"name": "Sabyasachi", "flipkart_seller_fashion_id": "flipkart_seller_womens_clothing_3"},
        {"name": "H&M", "flipkart_seller_fashion_id": "flipkart_seller_womens_clothing_4"},
        {"name": "Van Heusen", "flipkart_seller_fashion_id": "flipkart_seller_womens_clothing_5"}
    ],
    "kids-clothing": [
        {"name": "FirstCry", "flipkart_seller_fashion_id": "flipkart_seller_kids_clothing_1"},
        {"name": "Mothercare", "flipkart_seller_fashion_id": "flipkart_seller_kids_clothing_2"},
        {"name": "Hamleys", "flipkart_seller_fashion_id": "flipkart_seller_kids_clothing_3"},
        {"name": "Gini & Jony", "flipkart_seller_fashion_id": "flipkart_seller_kids_clothing_4"},
        {"name": "Lilliput", "flipkart_seller_fashion_id": "flipkart_seller_kids_clothing_5"}
    ],
    "footwear": [
        {"name": "Nike", "flipkart_seller_fashion_id": "flipkart_seller_footwear_1"},
        {"name": "Adidas", "flipkart_seller_fashion_id": "flipkart_seller_footwear_2"},
        {"name": "Woodland", "flipkart_seller_fashion_id": "flipkart_seller_footwear_3"},
        {"name": "Reebok", "flipkart_seller_fashion_id": "flipkart_seller_footwear_4"},
        {"name": "Puma", "flipkart_seller_fashion_id": "flipkart_seller_footwear_5"}
    ],
    "bags-backpacks": [
        {"name": "Wildcraft", "flipkart_seller_fashion_id": "flipkart_seller_bags_backpacks_1"},
        {"name": "American Tourister", "flipkart_seller_fashion_id": "flipkart_seller_bags_backpacks_2"},
        {"name": "Samsonite", "flipkart_seller_fashion_id": "flipkart_seller_bags_backpacks_3"},
        {"name": "Lavie", "flipkart_seller_fashion_id": "flipkart_seller_bags_backpacks_4"},
        {"name": "Baggit", "flipkart_seller_fashion_id": "flipkart_seller_bags_backpacks_5"}
    ],
    "watches": [
        {"name": "Titan", "flipkart_seller_fashion_id": "flipkart_seller_watches_1"},
        {"name": "Casio", "flipkart_seller_fashion_id": "flipkart_seller_watches_2"},
        {"name": "Rolex", "flipkart_seller_fashion_id": "flipkart_seller_watches_3"},
        {"name": "Seiko", "flipkart_seller_fashion_id": "flipkart_seller_watches_4"},
        {"name": "Fossil", "flipkart_seller_fashion_id": "flipkart_seller_watches_5"}
    ],
    "sunglasses": [
        {"name": "Ray-Ban", "flipkart_seller_fashion_id": "flipkart_seller_sunglasses_1"},
        {"name": "Oakley", "flipkart_seller_fashion_id": "flipkart_seller_sunglasses_2"},
        {"name": "Maui Jim", "flipkart_seller_fashion_id": "flipkart_seller_sunglasses_3"},
        {"name": "Fastrack", "flipkart_seller_fashion_id": "flipkart_seller_sunglasses_4"},
        {"name": "Police", "flipkart_seller_fashion_id": "flipkart_seller_sunglasses_5"}
    ],
    "hats-caps": [
        {"name": "New Era", "flipkart_seller_fashion_id": "flipkart_seller_hats_caps_1"},
        {"name": "Adidas", "flipkart_seller_fashion_id": "flipkart_seller_hats_caps_2"},
        {"name": "Nike", "flipkart_seller_fashion_id": "flipkart_seller_hats_caps_3"},
        {"name": "Reebok", "flipkart_seller_fashion_id": "flipkart_seller_hats_caps_4"},
        {"name": "Puma", "flipkart_seller_fashion_id": "flipkart_seller_hats_caps_5"}
    ],
    "jewelry": [
        {"name": "Tanishq", "flipkart_seller_fashion_id": "flipkart_seller_jewelry_1"},
        {"name": "Kalyan Jewellers", "flipkart_seller_fashion_id": "flipkart_seller_jewelry_2"},
        {"name": "Malabar Gold", "flipkart_seller_fashion_id": "flipkart_seller_jewelry_3"},
        {"name": "CaratLane", "flipkart_seller_fashion_id": "flipkart_seller_jewelry_4"},
        {"name": "Pendants", "flipkart_seller_fashion_id": "flipkart_seller_jewelry_5"}
    ],
    "sportswear": [
        {"name": "Decathlon", "flipkart_seller_fashion_id": "flipkart_seller_sportswear_1"},
        {"name": "Nike", "flipkart_seller_fashion_id": "flipkart_seller_sportswear_2"},
        {"name": "Adidas", "flipkart_seller_fashion_id": "flipkart_seller_sportswear_3"},
        {"name": "Puma", "flipkart_seller_fashion_id": "flipkart_seller_sportswear_4"},
        {"name": "Reebok", "flipkart_seller_fashion_id": "flipkart_seller_sportswear_5"}
    ]
}


# Function to generate seller and product data
def generate_seller_data(subcategory, seller_info, unique_product_counter):
    seller_data = []
    product_ids_used = set()  # Set to keep track of already used product IDs
    
    for seller in seller_info:
        seller_id = seller['flipkart_seller_fashion_id']
        # Generate 10 unique product ids for this seller
        product_ids = []
        while len(product_ids) < 10:
            product_id = f"flipkart_fashion_{subcategory}_{unique_product_counter}"
            if product_id not in product_ids_used:
                product_ids.append(product_id)
                product_ids_used.add(product_id)
                unique_product_counter += 1
        
        # Construct seller's data in required format
        seller_data.append({
            "retailer_id": seller_id,
            "retailer_name": seller['name'],
            "retailer_store_name": fake.company(),
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

