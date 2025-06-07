from rdflib import Graph, Namespace

def load_ontology():
    # Create one graph
    ontology_graph = Graph()

    # Parse the Amazon Ontology
    ontology_graph.parse("./ecommerce_ontology_amazon.ttl", format="turtle")

    # Parse the Flipkart ontology
    ontology_graph.parse("./ecommerce_ontology_flipkart.ttl", format="turtle")

    # Parse the Mappings
    ontology_graph.parse("./ecommerce_mapping.ttl", format="turtle")

    #Define namespaces 

    # Amazon Ontology Namespaces
    deltaNS = Namespace("http://delta.org#")
    amzNS = Namespace("http://delta.org/amazon#")       
    amzCustomerNS = Namespace("http://delta.org/amazon/CustomerNS#")
    amzOrderNS = Namespace("http://delta.org/amazon/OrderNS#")
    amzProductNS = Namespace("http://delta.org/amazon/ProductNS#")
    amzProductShippingOptionsNS = Namespace("http://delta.org/amazon/ProductShippingOptionsNS#")
    amzSellerNS = Namespace("http://delta.org/amazon/SellerNS#")

    flipNS = Namespace("http://delta.org/flipkart#")      # Second ontology
    flipCustomerNS = Namespace("http://delta.org/flipkart/CustomerNS#")
    flipItemNS = Namespace("http://delta.org/flipkart/ItemNS#")
    flipItemShippingOptionsNS = Namespace("http://delta.org/flipkart/ItemShippingOptionsNS#")
    flipOrderNS = Namespace("http://delta.org/flipkart/OrderNS#")
    flipSellerNS = Namespace("http://delta.org/flipkart/SellerNS#")

    # Bind prefixes (optional but recommended for nicer serialization)
    ontology_graph.bind("amzNS", amzNS)
    ontology_graph.bind("flipNS", flipNS)

    return ontology_graph, deltaNS, amzNS, amzCustomerNS, amzOrderNS, amzProductNS, amzProductShippingOptionsNS, amzSellerNS, flipNS, flipCustomerNS, flipItemNS, flipItemShippingOptionsNS, flipOrderNS, flipSellerNS