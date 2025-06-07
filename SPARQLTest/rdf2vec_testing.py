# json_to_sparql.py
import json

def json_to_sparql_prefixes(json_data):
    prefixes = ""
    for class_name, class_data in json_data.items():
        class_uri = class_data["id"]
        prefixes += f"@prefix {class_name.lower()}: <{class_uri}> .\n"
        for attr_name, attr_uri in class_data["attributes"].items():
            prefixes += f"@prefix {attr_name.lower()}: <{attr_uri}> .\n"
    return prefixes

####################################################

# query_model.py
from transformers import T5ForConditionalGeneration, T5Tokenizer
# from json_to_sparql import json_to_sparql_prefixes

    # Load the pre-trained transformer model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("yazdipour/text-to-sparql-t5-base")
tokenizer = T5Tokenizer.from_pretrained("yazdipour/text-to-sparql-t5-base")

def generate_sparql_query(ontology_json, natural_query):
    # Convert the JSON structure to SPARQL prefixes
    prefixes = json_to_sparql_prefixes(ontology_json)

    # Combine prefixes with the natural language query
    input_text = prefixes + natural_query

    # Tokenize the input
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate the SPARQL query
    outputs = model.generate(input_ids, max_length=50, num_beams=4, early_stopping=True)
    sparql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return sparql_query

########################################################

# main.py
from load_data import load_data
# from query_model import generate_sparql_query

# Load the data and the graph
full_graph = load_data()

# Define the ontology in JSON format (similar to the one you already have)
ontology_json = {
    "Product": {
        "id": "http://example.org#Product",
        "attributes": {
            "name": "http://example.org#name",
            "price": "http://example.org#price",
            "brand": "http://example.org#brand"
        }
    },
    "Item": {
        "id": "http://example2.org#Item",
        "attributes": {
            "itemName": "http://example2.org#itemName",
            "itemCost": "http://example2.org#itemCost",
            "manufacturer": "http://example2.org#manufacturer"
        }
    }
}

# Define the natural language query you want to convert to SPARQL
natural_query = "What is the price of Apple products?"
# Generate the SPARQL query using the transformer model
sparql_query = generate_sparql_query(ontology_json, natural_query)
# Print the generated SPARQL query
print(f"Generated SPARQL query: {sparql_query}")

# Execute the SPARQL query on the RDF graph (using rdflib)

# from rdflib import Graph

# result = full_graph.query(sparql_query)

# # Print the query results
# for row in result:
#     print(f"Product: {row.product}, Price: {row.price}")
