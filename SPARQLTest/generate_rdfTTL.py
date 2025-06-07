from load_data_amazon_flipkart import load_data
from owlrl import DeductiveClosure, OWLRL_Semantics
from rdflib import Graph, Namespace, URIRef, Literal, RDF
from load_ecommerce_ontology import load_ontology
import json
from rdflib.namespace import RDF, RDFS
from urllib.parse import quote

# Load the data graph
full_graph = load_data()

DeductiveClosure(OWLRL_Semantics).expand(full_graph)

# print(f"Graph after reasoning: {len(full_graph)} triples.")
deltaNS = Namespace("http://delta.org#")

# Amazon Namespaces
amzNS = Namespace("http://delta.org/amazon#")
amzProductNS = Namespace("http://delta.org/amazon/ProductNS#")
amzCustomerNS = Namespace("http://delta.org/amazon/CustomerNS#")
amzOrderNS = Namespace("http://delta.org/amazon/OrderNS#")
amzProductShippingOptionsNS = Namespace("http://delta.org/amazon/ProductShippingOptionsNS#")
amzSellerNS = Namespace("http://delta.org/amazon/SellerNS#")

# Flipkart Namespaces
flipNS = Namespace("http://delta.org/flipkart#")      
flipCustomerNS = Namespace("http://delta.org/flipkart/CustomerNS#")
flipItemNS = Namespace("http://delta.org/flipkart/ItemNS#")
flipItemShippingOptionsNS = Namespace("http://delta.org/flipkart/ItemShippingOptionsNS#")
flipOrderNS = Namespace("http://delta.org/flipkart/OrderNS#")
flipSellerNS = Namespace("http://delta.org/flipkart/SellerNS#")


# Namespaces defining
"""
PREFIX amzNS: <http://delta.org/amazon#>
PREFIX amzProductNS: <http://delta.org/amazon/ProductNS#>
PREFIX amzCustomerNS: <http://delta.org/amazon/CustomerNS#>
PREFIX amzOrderNS: <http://delta.org/amazon/OrderNS#>
PREFIX amzProductShippingOptionsNS: <http://delta.org/amazon/ProductShippingOptionsNS#>
PREFIX amzSellerNS: <http://delta.org/amazon/SellerNS#>

PREFIX flipNS: <http://delta.org/flipkart#>
PREFIX flipCustomerNS: <http://delta.org/flipkart/CustomerNS#>
PREFIX flipItemNS: <http://delta.org/flipkart/ItemNS#>
PREFIX flipItemShippingOptionsNS: <http://delta.org/flipkart/ItemShippingOptionsNS#>
PREFIX flipOrderNS: <http://delta.org/flipkart/OrderNS#>
PREFIX flipSellerNS: <http://delta.org/flipkart/SellerNS#>
"""

query = """
PREFIX amzNS: <http://delta.org/amazon#>
PREFIX amzProductNS: <http://delta.org/amazon/ProductNS#>

SELECT ?product ?productName ?price
WHERE {
  ?product a amzNS:Product .
  ?product amzProductNS:hasPrice ?priceNode .
  ?priceNode amzProductNS:price_amount ?price .
  OPTIONAL { ?product amzProductNS:product_name ?productName . }
  FILTER(?price >= 25 && ?price <= 100)
}
ORDER BY ?price
LIMIT 100
"""

results = full_graph.query(query)
print(results)
for row in results:
    product_name = row.product
    productName = row.productName
    price = row.price
    print(f"Product id: {product_name}")
    print(f"Product Name: {productName}")
    print(f"price: {price}")
    print("------------")

