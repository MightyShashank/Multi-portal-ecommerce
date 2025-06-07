# load_ontology.py
from rdflib import Graph, Namespace

def load_ontology():
    # Create one graph
    ontology_graph = Graph()

    # Parse the Amazon ontology
    ontology_graph.parse("./ecommerce_ontology_amazon.ttl", format="turtle")

    # Parse the Flipkart ontology
    ontology_graph.parse("./ecommerce_ontology_flipkart.ttl", format="turtle")

    # Parse the mappings
    ontology_graph.parse("./ecommerce_mapping.ttl", format="turtle")

    # Define namespaces
    EX_Amz = Namespace("http://delta.org/amazon#")       # First ontology
    EX_Flip = Namespace("http://delta.org/flipkart#")      # Second ontology

    # Bind prefixes (optional but recommended for nicer serialization)
    ontology_graph.bind("ex", EX_Amz)
    ontology_graph.bind("ex2", EX_Flip)

    return ontology_graph, EX_Amz, EX_Flip
