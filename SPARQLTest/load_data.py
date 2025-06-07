# load_data.py
from rdflib import Graph, Namespace, URIRef, Literal, RDF
from load_ontology import load_ontology

def load_data():
    ontology_graph, EX, EX2 = load_ontology()

    amazon_data = {
        "products": [
            {"id": "101", "name": "iPhone 14", "price": 799, "brand": "Apple"},
            {"id": "102", "name": "Pixel 8", "price": 699, "brand": "Google"}
        ]
    }

    products_data_another = {
        "items": [
            {"id": "201", "itemName": "Samsung ZFold5", "itemCost": 809, "manufacturer": "Samsung"},
            {"id": "202", "itemName": "Samsung S22", "itemCost": 659, "manufacturer": "Samsung"}
        ]
    }

    data_graph = Graph()
    data_graph.bind("ex", EX)
    data_graph.bind("ex2", EX2)

    BASE_Apple = "http://apple.org/product/"
    BASE_Samsung = "http://samsung.org/product/"

    for product in products_data["products"]:
        product_uri = URIRef(f"{BASE_Apple}{product['id']}")
        
        data_graph.add((product_uri, RDF.type, EX.Product))
        data_graph.add((product_uri, EX.name, Literal(product["name"])))
        data_graph.add((product_uri, EX.price, Literal(product["price"])))
        data_graph.add((product_uri, EX.brand, Literal(product["brand"])))
    
    for item in products_data_another["items"]:
        item_uri = URIRef(f"{BASE_Samsung}{item['id']}")

        data_graph.add((item_uri, RDF.type, EX2.Item))
        data_graph.add((item_uri, EX2.itemName, Literal(item["itemName"])))
        data_graph.add((item_uri, EX2.itemCost, Literal(item["itemCost"])))
        data_graph.add((item_uri, EX2.manufacturer, Literal(item["manufacturer"])))

    # Merge if you want full ontology + data
    full_graph = ontology_graph + data_graph

    # (Optional) serialize and save full_graph
    # full_graph.serialize(destination="full_graph_with_data.ttl", format="turtle")

    return full_graph  # or return full_graph if you want ontology too
