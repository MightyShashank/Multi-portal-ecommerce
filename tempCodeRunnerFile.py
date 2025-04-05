import json
import random
from fakeData.electronics.faker_electronics import Faker
from datetime import datetime, timedelta

fake = Faker()

# Function to generate a single fake product
def generate_fake_product():
    return {
        "id": fake.uuid4(),
        "name": fake.sentence(nb_words=3),
        "description": fake.paragraph(),
        "brand": fake.company(),
        "model_number": fake.bothify(text="???-####"),
        "category": random.choice(["Electronics", "Clothing", "Home", "Books", "Toys", "Beauty"]),
        "identifiers": {
            "sku": fake.bothify(text="SKU-#######"),
            "upc": fake.ean13(),
            "ean": fake.ean8(),
            "isbn": fake.isbn13() if random.choice([True, False]) else None
        },
        "price": {
            "amount": round(random.uniform(5, 1000), 2),
            "currency": random.choice(["USD", "EUR", "INR", "GBP"])
        },
        "availability": {
            "stock": random.randint(0, 100),
            "status": random.choice(["In Stock", "Out of Stock"]),
            "restock_date": fake.iso8601() if random.choice([True, False]) else None
        },
        "rating": {
            "average": round(random.uniform(1, 5), 1),
            "number_of_reviews": random.randint(0, 500)
        },
        "dimensions": {
            "height_cm": round(random.uniform(5, 100), 2),
            "width_cm": round(random.uniform(5, 100), 2),
            "depth_cm": round(random.uniform(5, 100), 2),
            "weight_kg": round(random.uniform(0.1, 10), 2)
        },
        "materials": [fake.word() for _ in range(random.randint(1, 3))],
        "colors": [fake.color_name() for _ in range(random.randint(1, 5))],
        "features": [fake.sentence(nb_words=5) for _ in range(random.randint(2, 6))],
        "images": [
            {"url": fake.image_url(), "alt_text": fake.sentence(nb_words=4)}
            for _ in range(random.randint(1, 4))
        ],
        "seller": {
            "id": fake.uuid4(),
            "name": fake.company(),
            "rating": round(random.uniform(1, 5), 1)
        }
    }

# Generate a list of fake products
fake_products = [generate_fake_product() for _ in range(10)]  # Change 10 to any number

# Save to a JSON file
with open("fake_products.json", "w") as f:
    json.dump(fake_products, f, indent=4)

print("Fake product data generated and saved to fake_products.json!")
