from flask import Flask, request, jsonify
from rdflib import Graph, Namespace
from owlrl import DeductiveClosure, OWLRL_Semantics
import json

# Load your data and ontology (from your existing code)
from load_data_amazon_flipkart import load_data
from load_ecommerce_ontology import load_ontology

# Initialize Flask app
app = Flask(__name__)

# Global variable for the RDF graph
full_graph = None

# Load the data graph once when the server starts
def initialize_graph():
    global full_graph
    if full_graph is None:
        # Load data and apply reasoning only once during initialization
        full_graph = load_data()
        DeductiveClosure(OWLRL_Semantics).expand(full_graph)
        print("Graph initialized and reasoning applied.")

# Define the namespaces
amzNS = Namespace("http://delta.org/amazon#")
amzProductNS = Namespace("http://delta.org/amazon/ProductNS#")

# Define a function to run SPARQL query
def execute_sparql_query(query):
    try:
        results = full_graph.query(query)
        result_list = []
        for row in results:
            result_dict = {}
            for var in results.vars:  # Loop through the variable names (e.g., ?product, ?productName, ?price)
                result_dict[str(var)] = str(row[var])  # Convert each result value to string and store in the dictionary
            result_list.append(result_dict)
        return result_list
    except Exception as e:
        return str(e)

# Endpoint to accept SPARQL query via GET or POST
@app.route('/sparql', methods=['GET', 'POST'])
def sparql():
    # Ensure the graph is initialized once
    initialize_graph()

    if request.method == 'POST':
        query = request.json.get('query', '')
    else:
        query = request.args.get('query', '')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = execute_sparql_query(query)
    return jsonify(results)

if __name__ == '__main__':
    # Initialize the graph when the server starts
    initialize_graph()
    app.run(debug=True, host='0.0.0.0', port=5000)
