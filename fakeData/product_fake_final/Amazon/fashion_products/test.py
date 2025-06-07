import json

with open('./fake_products_fashion.json', 'r') as f:
    products_data = json.load(f)

count = 0

def find_null_seller():
    """
    Takes a product_id and searches for it in the products_data.
    Increments the global 'count' if the seller is None.
    """
    global count  # Declare that we're using the global 'count' variable
    for product in products_data:
        if product.get('seller', None) is None:  # Checks if 'seller' is None
            count += 1  # Increment the global count
    return count

print(find_null_seller())
