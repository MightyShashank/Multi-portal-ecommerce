from rdflib import Graph, Namespace, URIRef, Literal, RDF, XSD
from load_ecommerce_ontology import load_ontology
import json
from rdflib.namespace import RDF, RDFS
from urllib.parse import quote
from decimal import Decimal
# subClassOf

def load_data():
    ontology_graph, deltaNS, amzNS, amzCustomerNS, amzOrderNS, amzProductNS, amzProductShippingOptionsNS, amzSellerNS, flipNS, flipCustomerNS, flipItemNS, flipItemShippingOptionsNS, flipOrderNS, flipSellerNS = load_ontology()

    with open('./Amazon/fake_products_electronics.json', 'r') as file:
        products_amazon_electronics = json.load(file) # its a list of product dicts

    with open('./Amazon/fake_products_fashion.json', 'r') as file:
        products_amazon_fashion = json.load(file)

    with open('./Flipkart/fake_products_electronics.json', 'r') as file:
        products_flipkart_electronics = json.load(file) # its a list of product dicts

    with open('./Flipkart/fake_products_fashion.json', 'r') as file:
        products_flipkart_fashion = json.load(file)

    amazon_data = {
        "products_electronics": products_amazon_electronics,
        "products_fashion": products_amazon_fashion
    }

    flipkart_data = {
        "products_electronics": products_flipkart_electronics,
        "products_fashion": products_flipkart_fashion
    }

    data_graph = Graph()
    data_graph.bind("amzNS", amzNS)
    data_graph.bind("amzCustomerNS", amzCustomerNS)
    data_graph.bind("amzOrderNS", amzOrderNS)
    data_graph.bind("amzProductNS", amzProductNS)
    data_graph.bind("amzProductShippingOptionsNS", amzProductShippingOptionsNS)
    data_graph.bind("amzSellerNS", amzSellerNS)

    data_graph.bind("flipNS", flipNS)
    data_graph.bind("flipCustomerNS", flipCustomerNS)
    data_graph.bind("flipItemNS", flipItemNS)
    data_graph.bind("flipItemShippingOptionsNS", flipItemShippingOptionsNS)
    data_graph.bind("flipOrderNS", flipOrderNS)
    data_graph.bind("flipSellerNS", flipSellerNS)
    
    # DeductiveClosure(OWLRL_Semantics).expand(full_graph)
    BASE_Amazon = "http://delta.org/amazon/"
    BASE_Flipkart = "http://delta.org/flipkart/"
    BASE_Delta = "http://delta.org"

    BASE_Amazon = URIRef(BASE_Amazon)
    BASE_Flipkart = URIRef(BASE_Flipkart)
    BASE_Delta = URIRef(BASE_Delta)

    data_graph.add((BASE_Amazon, RDFS.subClassOf, deltaNS.Ecommerce))
    data_graph.add((BASE_Flipkart, RDFS.subClassOf, deltaNS.Ecommerce))
    ###################### Populate Amazon #############################
    # Electronics:
    for product in amazon_data['products_electronics']:
        product_uri = URIRef(f"{BASE_Amazon}{product['id']}")
  
        # data_graph.add((product_uri, EX.madeBy, brand_uri))  # 🔥 relation here
        # data_graph.add((product_uri, EX.name, Literal(product["name"])))
        
        data_graph.add((product_uri, RDF.type, amzNS.Product))
        data_graph.add((BASE_Amazon, amzNS.hasProduct, product_uri))
        data_graph.add((product_uri, amzProductNS.id, Literal(product['id'])))
        data_graph.add((product_uri, amzProductNS.description, Literal(product['description'])))
        data_graph.add((product_uri, amzProductNS.product_name, Literal(product['product_name'])))
        data_graph.add((product_uri, amzProductNS.model_number, Literal(product['model_number'])))
        data_graph.add((product_uri, amzProductNS.color, Literal(product['color'])))
        data_graph.add((product_uri, amzProductNS.features, Literal(product['features'])))
        data_graph.add((product_uri, amzProductNS.images, Literal(product['images'])))

        # Brand
        brand_uri = URIRef(f"{BASE_Amazon}{quote(product['brand']['brand_name'])}")
        data_graph.add((brand_uri, RDF.type, amzProductNS.Brand))
        data_graph.add((brand_uri, amzProductNS.brand_name, Literal(product['brand']['brand_name'])))
        data_graph.add((BASE_Amazon, amzNS.hasBrand, brand_uri))

        # category and Sub-category
        category_uri = URIRef(f"{BASE_Amazon}{product['category']['category_name']}")
        data_graph.add((category_uri, RDF.type, amzProductNS.Category))
        data_graph.add((category_uri, amzProductNS.category_name, Literal(product['category']['category_name'])))
        data_graph.add((BASE_Amazon, amzNS.hasCategory, category_uri))

        sub_category_uri = URIRef(f"{BASE_Amazon}{product['category']['category_name']}/{product['category']['sub_category']['sub-_category_name']}")
        data_graph.add((sub_category_uri, RDF.type, amzProductNS.SubCategory))
        data_graph.add((sub_category_uri, amzProductNS.sub_category_name, Literal(product['category']['sub_category']['sub-_category_name'])))

        # Product, Brand, Category, sub-category relationships
        data_graph.add((product_uri, amzNS.hasBrand, brand_uri))
        data_graph.add((brand_uri, amzProductNS.producesProduct, product_uri))
        data_graph.add((sub_category_uri, amzProductNS.hasProduct, product_uri))
        data_graph.add((category_uri, amzProductNS.hasSubCategory, sub_category_uri))
        data_graph.add((category_uri, amzProductNS.hasProduct, product_uri))
        data_graph.add((product_uri, amzProductNS.hasCategory, category_uri))

        price_uri = URIRef(f"{BASE_Amazon}{product['id']}_price")
        data_graph.add((price_uri, RDF.type, amzProductNS.Price))
        data_graph.add((price_uri, amzProductNS.price_amount, Literal(str(Decimal(str(product['price']['amount']))), datatype=XSD.decimal)))
        data_graph.add((price_uri, amzProductNS.price_currency, Literal(product['price']['currency'])))
        data_graph.add((product_uri, amzProductNS.hasPrice, price_uri))

        availability_uri = URIRef(f"{BASE_Amazon}{product['id']}_availability")
        data_graph.add((availability_uri, RDF.type, amzProductNS.Availability))
        data_graph.add((availability_uri, amzProductNS.availability_stock, Literal(product['availability']['stock'])))
        data_graph.add((availability_uri, amzProductNS.availability_status, Literal(product['availability']['status'])))
        data_graph.add((availability_uri, amzProductNS.availability_restock_date, Literal(product['availability']['restock_date'])))
        data_graph.add((product_uri, amzProductNS.hasAvailability, availability_uri))

        product_return_policy_uri = URIRef(f"{BASE_Amazon}{product['id']}_return_policy")
        data_graph.add((product_return_policy_uri, RDF.type, amzProductNS.Return_Policy))

        return_period_days = product.get("return_policy", {}).get("return_period_days")
        if return_period_days is not None:
            data_graph.add((product_return_policy_uri,amzProductNS.return_policy_return_period_days,Literal(return_period_days)))

        return_conditions = product.get("return_policy", {}).get("conditions")
        if return_conditions is not None:
            data_graph.add((
                product_return_policy_uri,
                amzProductNS.return_policy_conditions,
                Literal(return_conditions)
            ))
        data_graph.add((product_return_policy_uri, amzProductNS.return_policy_is_return_eligible,  Literal(product['return_policy']['isReturnEligible'])))
        product_return_policy_return_fee_uri = URIRef(f"{BASE_Amazon}{product['id']}_return_policy/return_fee")
        data_graph.add((product_return_policy_return_fee_uri, RDF.type, amzProductNS.Return_Fee))
        return_fee_price = product.get("return_policy", {}).get("return_fee", {}).get("return_fee_price")
        if return_fee_price is not None:
            data_graph.add((
                product_return_policy_return_fee_uri,
                amzProductNS.return_fee_price,
                Literal(str(Decimal(str(return_fee_price))), datatype=XSD.decimal)
            ))
        return_fee_currency = product.get("return_policy", {}).get("return_fee", {}).get("return_fee_currency")
        if return_fee_currency is not None:
            data_graph.add((
                product_return_policy_return_fee_uri,
                amzProductNS.return_fee_currency,
                Literal(return_fee_currency)
            ))
        data_graph.add((product_return_policy_uri, amzProductNS.hasReturnFee, product_return_policy_return_fee_uri))
        data_graph.add((product_uri, amzProductNS.hasReturnPolicy, product_return_policy_uri))

        # Rating
        product_rating_uri = URIRef(f"{BASE_Amazon}{product['id']}_rating")
        data_graph.add((product_rating_uri, RDF.type, amzProductNS.hasRating))
        data_graph.add((product_uri, amzProductNS.hasRating, product_rating_uri))
        data_graph.add((product_rating_uri, amzProductNS.rating_average, Literal(str(Decimal(str(product['rating']['rating_average']))), datatype=XSD.decimal)))
        data_graph.add((product_rating_uri, amzProductNS.rating_number_of_reviews, Literal(product['rating']['number_of_reviews'])))

        # Dimensions 
        product_dimensions_uri = URIRef(f"{BASE_Amazon}{product['id']}_dimensions")
        data_graph.add((product_dimensions_uri, RDF.type, amzProductNS.Dimensions))
        data_graph.add((product_uri, amzProductNS.hasDimensions, product_dimensions_uri))
        data_graph.add((product_dimensions_uri, amzProductNS.dimensions_height_cm, Literal(str(Decimal(str(product['dimensions']['height_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, amzProductNS.dimensions_width_cm, Literal(str(Decimal(str(product['dimensions']['width_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, amzProductNS.dimensions_depth_cm, Literal(str(Decimal(str(product['dimensions']['depth_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, amzProductNS.dimensions_weight_cm, Literal(str(Decimal(str(product['dimensions']['weight_kg']))), datatype=XSD.decimal)))

        # Shipping Options
        product_shipping_options_uri = URIRef(f"{BASE_Amazon}{product['id']}_shipping_options")
        data_graph.add((product_shipping_options_uri, RDF.type, amzProductNS.Shipping_Options))
        product_shipping_options_uri_price = URIRef(f"{BASE_Amazon}{product['id']}_shipping_options_price")
        product_shipping_options_uri_delivery = URIRef(f"{BASE_Amazon}{product['id']}_shipping_options_delivery")
        data_graph.add((product_shipping_options_uri_price, RDF.type, amzProductShippingOptionsNS.Price))
        data_graph.add((product_shipping_options_uri_delivery, RDF.type, amzProductShippingOptionsNS.Estimated_Delivery_Time))
        data_graph.add((product_uri, amzProductNS.hasShippingOptions, product_shipping_options_uri))
        data_graph.add((product_shipping_options_uri, amzProductNS.shipping_options_method, Literal(product['shipping_options']['method'])))
        data_graph.add((product_shipping_options_uri, amzProductNS.hasShippingPrice, product_shipping_options_uri_price))
        data_graph.add((product_shipping_options_uri, amzProductNS.hasDeliveryTime, product_shipping_options_uri_delivery))
        data_graph.add((product_shipping_options_uri_price, amzProductShippingOptionsNS.shipping_options_price_cost, Literal(str(Decimal(str(product['shipping_options']['price']['cost']))), datatype=XSD.decimal)))
        data_graph.add((product_shipping_options_uri_price, amzProductShippingOptionsNS.shipping_options_price_currency, Literal(product['shipping_options']['price']['currency'])))
        data_graph.add((product_shipping_options_uri_delivery, amzProductShippingOptionsNS.shipping_options_estimated_delivery_time_delivery_time, Literal(product['shipping_options']['estimated_delivery_time']['delivery_time'])))
        data_graph.add((product_shipping_options_uri_delivery, amzProductShippingOptionsNS.shipping_options_estimated_delivery_time_metric, Literal(product['shipping_options']['estimated_delivery_time']['Metric'])))

        # Seller
        seller_uri = URIRef(f"{BASE_Amazon}seller/{product['seller']['seller_id']}")
        data_graph.add((seller_uri, RDF.type, amzNS.Seller))
        data_graph.add((product_uri, amzProductNS.hasSeller, seller_uri))
        data_graph.add((seller_uri, amzSellerNS.sells, product_uri))


    # Fashion
    for product in amazon_data['products_fashion']:
        product_uri = URIRef(f"{BASE_Amazon}{product['id']}")
  
        # data_graph.add((product_uri, EX.madeBy, brand_uri))  # 🔥 relation here
        # data_graph.add((product_uri, EX.name, Literal(product["name"])))
        
        data_graph.add((product_uri, RDF.type, amzNS.Product))
        data_graph.add((BASE_Amazon, amzNS.hasProduct, product_uri))
        data_graph.add((product_uri, amzProductNS.id, Literal(product['id'])))
        data_graph.add((product_uri, amzProductNS.description, Literal(product['description'])))
        data_graph.add((product_uri, amzProductNS.product_name, Literal(product['product_name'])))
        data_graph.add((product_uri, amzProductNS.model_number, Literal(product['model_number'])))
        data_graph.add((product_uri, amzProductNS.color, Literal(product['color'])))
        data_graph.add((product_uri, amzProductNS.features, Literal(product['features'])))
        data_graph.add((product_uri, amzProductNS.images, Literal(product['images'])))

        # Brand
        brand_uri = URIRef(f"{BASE_Amazon}{quote(product['brand']['brand_name'])}")
        data_graph.add((brand_uri, RDF.type, amzProductNS.Brand))
        data_graph.add((brand_uri, amzProductNS.brand_name, Literal(product['brand']['brand_name'])))
        data_graph.add((BASE_Amazon, amzNS.hasBrand, brand_uri))

        # category and Sub-category
        category_uri = URIRef(f"{BASE_Amazon}{product['category']['category_name']}")
        data_graph.add((category_uri, RDF.type, amzProductNS.Category))
        data_graph.add((category_uri, amzProductNS.category_name, Literal(product['category']['category_name'])))
        data_graph.add((BASE_Amazon, amzNS.hasCategory, category_uri))

        sub_category_uri = URIRef(f"{BASE_Amazon}{product['category']['category_name']}/{product['category']['sub_category']['sub-_category_name']}")
        data_graph.add((sub_category_uri, RDF.type, amzProductNS.SubCategory))
        data_graph.add((sub_category_uri, amzProductNS.sub_category_name, Literal(product['category']['sub_category']['sub-_category_name'])))

        # Product, Brand, Category, sub-category relationships
        data_graph.add((product_uri, amzNS.hasBrand, brand_uri))
        data_graph.add((brand_uri, amzProductNS.producesProduct, product_uri))
        data_graph.add((sub_category_uri, amzProductNS.hasProduct, product_uri))
        data_graph.add((category_uri, amzProductNS.hasSubCategory, sub_category_uri))
        data_graph.add((category_uri, amzProductNS.hasProduct, product_uri))
        data_graph.add((product_uri, amzProductNS.hasCategory, category_uri))

        price_uri = URIRef(f"{BASE_Amazon}{product['id']}_price")
        data_graph.add((price_uri, RDF.type, amzProductNS.Price))
        data_graph.add((price_uri, amzProductNS.price_amount, Literal(str(Decimal(str(product['price']['amount']))), datatype=XSD.decimal)))
        data_graph.add((price_uri, amzProductNS.price_currency, Literal(product['price']['currency'])))
        data_graph.add((product_uri, amzProductNS.hasPrice, price_uri))

        availability_uri = URIRef(f"{BASE_Amazon}{product['id']}_availability")
        data_graph.add((availability_uri, RDF.type, amzProductNS.Availability))
        data_graph.add((availability_uri, amzProductNS.availability_stock, Literal(product['availability']['stock'])))
        data_graph.add((availability_uri, amzProductNS.availability_status, Literal(product['availability']['status'])))
        data_graph.add((availability_uri, amzProductNS.availability_restock_date, Literal(product['availability']['restock_date'])))
        data_graph.add((product_uri, amzProductNS.hasAvailability, availability_uri))

        product_return_policy_uri = URIRef(f"{BASE_Amazon}{product['id']}_return_policy")
        data_graph.add((product_return_policy_uri, RDF.type, amzProductNS.Return_Policy))

        return_period_days = product.get("return_policy", {}).get("return_period_days")
        if return_period_days is not None:
            data_graph.add((product_return_policy_uri,amzProductNS.return_policy_return_period_days,Literal(return_period_days)))

        return_conditions = product.get("return_policy", {}).get("conditions")
        if return_conditions is not None:
            data_graph.add((
                product_return_policy_uri,
                amzProductNS.return_policy_conditions,
                Literal(return_conditions)
            ))
        data_graph.add((product_return_policy_uri, amzProductNS.return_policy_is_return_eligible,  Literal(product['return_policy']['isReturnEligible'])))
        product_return_policy_return_fee_uri = URIRef(f"{BASE_Amazon}{product['id']}_return_policy/return_fee")
        data_graph.add((product_return_policy_return_fee_uri, RDF.type, amzProductNS.Return_Fee))
        return_fee_price = product.get("return_policy", {}).get("return_fee", {}).get("return_fee_price")
        if return_fee_price is not None:
            data_graph.add((
                product_return_policy_return_fee_uri,
                amzProductNS.return_fee_price,
                Literal(str(Decimal(str(return_fee_price))), datatype=XSD.decimal)
            ))
        return_fee_currency = product.get("return_policy", {}).get("return_fee", {}).get("return_fee_currency")
        if return_fee_currency is not None:
            data_graph.add((
                product_return_policy_return_fee_uri,
                amzProductNS.return_fee_currency,
                Literal(return_fee_currency)
            ))
        data_graph.add((product_return_policy_uri, amzProductNS.hasReturnFee, product_return_policy_return_fee_uri))
        data_graph.add((product_uri, amzProductNS.hasReturnPolicy, product_return_policy_uri))

        # Rating
        product_rating_uri = URIRef(f"{BASE_Amazon}{product['id']}_rating")
        data_graph.add((product_rating_uri, RDF.type, amzProductNS.hasRating))
        data_graph.add((product_uri, amzProductNS.hasRating, product_rating_uri))
        data_graph.add((product_rating_uri, amzProductNS.rating_average, Literal(str(Decimal(str(product['rating']['rating_average']))), datatype=XSD.decimal)))
        data_graph.add((product_rating_uri, amzProductNS.rating_number_of_reviews, Literal(product['rating']['number_of_reviews'])))

        # Dimensions 
        product_dimensions_uri = URIRef(f"{BASE_Amazon}{product['id']}_dimensions")
        data_graph.add((product_dimensions_uri, RDF.type, amzProductNS.Dimensions))
        data_graph.add((product_uri, amzProductNS.hasDimensions, product_dimensions_uri))
        data_graph.add((product_dimensions_uri, amzProductNS.dimensions_height_cm, Literal(str(Decimal(str(product['dimensions']['height_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, amzProductNS.dimensions_width_cm, Literal(str(Decimal(str(product['dimensions']['width_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, amzProductNS.dimensions_depth_cm, Literal(str(Decimal(str(product['dimensions']['depth_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, amzProductNS.dimensions_weight_cm, Literal(str(Decimal(str(product['dimensions']['weight_kg']))), datatype=XSD.decimal)))

        # Shipping Options
        product_shipping_options_uri = URIRef(f"{BASE_Amazon}{product['id']}_shipping_options")
        data_graph.add((product_shipping_options_uri, RDF.type, amzProductNS.Shipping_Options))
        product_shipping_options_uri_price = URIRef(f"{BASE_Amazon}{product['id']}_shipping_options_price")
        product_shipping_options_uri_delivery = URIRef(f"{BASE_Amazon}{product['id']}_shipping_options_delivery")
        data_graph.add((product_shipping_options_uri_price, RDF.type, amzProductShippingOptionsNS.Price))
        data_graph.add((product_shipping_options_uri_delivery, RDF.type, amzProductShippingOptionsNS.Estimated_Delivery_Time))
        data_graph.add((product_uri, amzProductNS.hasShippingOptions, product_shipping_options_uri))
        data_graph.add((product_shipping_options_uri, amzProductNS.shipping_options_method, Literal(product['shipping_options']['method'])))
        data_graph.add((product_shipping_options_uri, amzProductNS.hasShippingPrice, product_shipping_options_uri_price))
        data_graph.add((product_shipping_options_uri, amzProductNS.hasDeliveryTime, product_shipping_options_uri_delivery))
        data_graph.add((product_shipping_options_uri_price, amzProductShippingOptionsNS.shipping_options_price_cost, Literal(str(Decimal(str(product['shipping_options']['price']['cost']))), datatype=XSD.decimal)))
        data_graph.add((product_shipping_options_uri_price, amzProductShippingOptionsNS.shipping_options_price_currency, Literal(product['shipping_options']['price']['currency'])))
        data_graph.add((product_shipping_options_uri_delivery, amzProductShippingOptionsNS.shipping_options_estimated_delivery_time_delivery_time, Literal(product['shipping_options']['estimated_delivery_time']['delivery_time'])))
        data_graph.add((product_shipping_options_uri_delivery, amzProductShippingOptionsNS.shipping_options_estimated_delivery_time_metric, Literal(product['shipping_options']['estimated_delivery_time']['Metric'])))

        # Seller
        seller_uri = URIRef(f"{BASE_Amazon}seller/{product['seller']['seller_id']}")
        data_graph.add((seller_uri, RDF.type, amzNS.Seller))
        data_graph.add((product_uri, amzProductNS.hasSeller, seller_uri))
        data_graph.add((seller_uri, amzSellerNS.sells, product_uri))


    ############################### Flipkart ########################################

    #Electronics
    for product in flipkart_data['products_electronics']:
        product_uri = URIRef(f"{BASE_Flipkart}{product['id']}")
  
        # data_graph.add((product_uri, EX.madeBy, brand_uri))  # 🔥 relation here
        # data_graph.add((product_uri, EX.name, Literal(product["name"])))
        
        data_graph.add((product_uri, RDF.type, amzNS.Item))
        data_graph.add((BASE_Flipkart, flipNS.hasItem, product_uri))
        data_graph.add((product_uri, flipItemNS.id, Literal(product['id'])))
        data_graph.add((product_uri, flipItemNS.description, Literal(product['description'])))
        data_graph.add((product_uri, flipItemNS.item_name, Literal(product['product_name'])))
        data_graph.add((product_uri, flipItemNS.model_number, Literal(product['model_number'])))
        data_graph.add((product_uri, flipItemNS.color, Literal(product['color'])))
        data_graph.add((product_uri, flipItemNS.features, Literal(product['features'])))
        data_graph.add((product_uri, flipItemNS.images, Literal(product['images'])))

        # Brand
        brand_uri = URIRef(f"{BASE_Flipkart}{quote(product['brand']['brand_name'])}")
        data_graph.add((brand_uri, RDF.type, flipItemNS.Producer))
        data_graph.add((brand_uri, flipItemNS.producer_name, Literal(product['brand']['brand_name'])))
        data_graph.add((BASE_Flipkart, flipNS.hasProducer, brand_uri))

        # category and Sub-category
        category_uri = URIRef(f"{BASE_Flipkart}{product['category']['category_name']}")
        data_graph.add((category_uri, RDF.type, flipItemNS.Group))
        data_graph.add((category_uri, flipItemNS.group_name, Literal(product['category']['category_name'])))
        data_graph.add((BASE_Flipkart, flipNS.hasGroup, category_uri))

        sub_category_uri = URIRef(f"{BASE_Flipkart}{product['category']['category_name']}/{product['category']['sub_category']['sub-_category_name']}")
        data_graph.add((sub_category_uri, RDF.type, flipItemNS.SubGroup))
        data_graph.add((sub_category_uri, flipItemNS.sub_group_name, Literal(product['category']['sub_category']['sub-_category_name'])))

        # Product, Brand, Category, sub-category relationships
        data_graph.add((product_uri, flipNS.hasProducer, brand_uri))
        data_graph.add((brand_uri, flipItemNS.producesItem, product_uri))
        data_graph.add((sub_category_uri, flipItemNS.hasItem, product_uri))
        data_graph.add((category_uri, flipItemNS.hasSubGroup, sub_category_uri))
        data_graph.add((category_uri, flipItemNS.hasItem, product_uri))
        data_graph.add((product_uri, flipItemNS.hasGroup, category_uri))

        price_uri = URIRef(f"{BASE_Flipkart}{product['id']}_price")
        data_graph.add((price_uri, RDF.type, flipItemNS.salePrice))
        data_graph.add((price_uri, flipItemNS.salePrice_amount, Literal(str(Decimal(str(product['price']['amount']))), datatype=XSD.decimal)))
        data_graph.add((price_uri, flipItemNS.price_currency, Literal(product['price']['currency'])))
        data_graph.add((product_uri, flipItemNS.hassalePrice, price_uri))

        availability_uri = URIRef(f"{BASE_Flipkart}{product['id']}_availability")
        data_graph.add((availability_uri, RDF.type, flipItemNS.stockStatus))
        data_graph.add((availability_uri, flipItemNS.stockStatus_stock, Literal(product['availability']['stock'])))
        data_graph.add((availability_uri, flipItemNS.stockStatus_status, Literal(product['availability']['status'])))
        data_graph.add((availability_uri, flipItemNS.stockStatus_restock_date, Literal(product['availability']['restock_date'])))
        data_graph.add((product_uri, flipItemNS.hasstockStatus, availability_uri))

        product_return_policy_uri = URIRef(f"{BASE_Flipkart}{product['id']}_return_policy")
        data_graph.add((product_return_policy_uri, RDF.type, flipItemNS.Return_Policy))

        return_period_days = product.get("return_policy", {}).get("return_period_days")
        if return_period_days is not None:
            data_graph.add((product_return_policy_uri,flipItemNS.Return_Rules_return_period_days, Literal(return_period_days)))

        return_conditions = product.get("return_policy", {}).get("conditions")
        if return_conditions is not None:
            data_graph.add((product_return_policy_uri,flipItemNS.Return_Rules_conditions,Literal(return_conditions)))

        data_graph.add((product_return_policy_uri, flipItemNS.Return_Rules_is_return_eligible,  Literal(product['return_policy']['isReturnEligible'])))

        product_return_policy_return_fee_uri = URIRef(f"{BASE_Flipkart}{product['id']}_return_policy/return_fee")
        data_graph.add((product_return_policy_return_fee_uri, RDF.type, flipItemNS.Return_Fee))

        return_fee_price = product.get("return_policy", {}).get("return_fee", {}).get("return_fee_price")
        if return_fee_price is not None:
            data_graph.add((
                product_return_policy_return_fee_uri,
                flipItemNS.return_fee_salePrice,
                Literal(str(Decimal(str(return_fee_price))), datatype=XSD.decimal)
            ))
        return_fee_currency = product.get("return_policy", {}).get("return_fee", {}).get("return_fee_currency")
        if return_fee_currency is not None:
            data_graph.add((
                product_return_policy_return_fee_uri,
                flipItemNS.return_fee_currency,
                Literal(return_fee_currency)
            ))
        data_graph.add((product_return_policy_uri, flipItemNS.hasReturnFee, product_return_policy_return_fee_uri))
        data_graph.add((product_uri, flipItemNS.hasReturnPolicy, product_return_policy_uri))

        # Rating
        product_rating_uri = URIRef(f"{BASE_Flipkart}{product['id']}_rating")
        data_graph.add((product_rating_uri, RDF.type, flipItemNS.hasRating))
        data_graph.add((product_uri, flipItemNS.hasRating, product_rating_uri))
        data_graph.add((product_rating_uri, flipItemNS.rating_average, Literal(str(Decimal(str(product['rating']['rating_average']))), datatype=XSD.decimal)))
        data_graph.add((product_rating_uri, flipItemNS.rating_number_of_reviews, Literal(product['rating']['number_of_reviews'])))

        # Dimensions 
        product_dimensions_uri = URIRef(f"{BASE_Flipkart}{product['id']}_dimensions")
        data_graph.add((product_dimensions_uri, RDF.type, flipItemNS.Dimensions))
        data_graph.add((product_uri, flipItemNS.hasDimensions, product_dimensions_uri))
        data_graph.add((product_dimensions_uri, flipItemNS.dimensions_height_cm, Literal(str(Decimal(str(product['dimensions']['height_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, flipItemNS.dimensions_width_cm, Literal(str(Decimal(str(product['dimensions']['width_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, flipItemNS.dimensions_depth_cm, Literal(str(Decimal(str(product['dimensions']['depth_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, flipItemNS.dimensions_weight_cm, Literal(str(Decimal(str(product['dimensions']['weight_kg']))), datatype=XSD.decimal)))

        # Shipping Options
        product_shipping_options_uri = URIRef(f"{BASE_Flipkart}{product['id']}_shipping_options")
        data_graph.add((product_shipping_options_uri, RDF.type, flipItemNS.Shipping_Methods))
        product_shipping_options_uri_price = URIRef(f"{BASE_Flipkart}{product['id']}_shipping_options_price")
        product_shipping_options_uri_delivery = URIRef(f"{BASE_Flipkart}{product['id']}_shipping_options_delivery")
        data_graph.add((product_shipping_options_uri_price, RDF.type, flipItemShippingOptionsNS.salePrice))
        data_graph.add((product_shipping_options_uri_delivery, RDF.type, flipItemShippingOptionsNS.Estimated_Delivery_Time))
        data_graph.add((product_uri, flipItemNS.hasShippingOptions, product_shipping_options_uri))
        data_graph.add((product_shipping_options_uri, flipItemNS.Shipping_Methods_method, Literal(product['shipping_options']['method'])))
        data_graph.add((product_shipping_options_uri, flipItemNS.hasShippingsalePrice, product_shipping_options_uri_price))
        data_graph.add((product_shipping_options_uri, flipItemNS.hasDeliveryTime, product_shipping_options_uri_delivery))
        data_graph.add((product_shipping_options_uri_price, flipItemShippingOptionsNS.Shipping_Methods_salePrice_cost, Literal(str(Decimal(str(product['shipping_options']['price']['cost']))), datatype=XSD.decimal)))
        data_graph.add((product_shipping_options_uri_price, flipItemShippingOptionsNS.Shipping_Methods_salePrice_currency, Literal(product['shipping_options']['price']['currency'])))
        data_graph.add((product_shipping_options_uri_delivery, flipItemShippingOptionsNS.Shipping_Methods_estimated_delivery_time_delivery_time, Literal(product['shipping_options']['estimated_delivery_time']['delivery_time'])))
        data_graph.add((product_shipping_options_uri_delivery, flipItemShippingOptionsNS.Shipping_Methods_estimated_delivery_time_metric, Literal(product['shipping_options']['estimated_delivery_time']['Metric'])))

        # Seller
        seller_uri = URIRef(f"{BASE_Flipkart}seller/{product['seller']['retailer_id']}")
        data_graph.add((seller_uri, RDF.type, flipNS.Seller))
        data_graph.add((product_uri, flipItemNS.hasSeller, seller_uri))
        data_graph.add((seller_uri, flipSellerNS.sells, product_uri))

    for product in flipkart_data['products_fashion']:
        product_uri = URIRef(f"{BASE_Flipkart}{product['id']}")
  
        # data_graph.add((product_uri, EX.madeBy, brand_uri))  # 🔥 relation here
        # data_graph.add((product_uri, EX.name, Literal(product["name"])))
        
        data_graph.add((product_uri, RDF.type, amzNS.Item))
        data_graph.add((BASE_Flipkart, flipNS.hasItem, product_uri))
        data_graph.add((product_uri, flipItemNS.id, Literal(product['id'])))
        data_graph.add((product_uri, flipItemNS.description, Literal(product['description'])))
        data_graph.add((product_uri, flipItemNS.item_name, Literal(product['product_name'])))
        data_graph.add((product_uri, flipItemNS.model_number, Literal(product['model_number'])))
        data_graph.add((product_uri, flipItemNS.color, Literal(product['color'])))
        data_graph.add((product_uri, flipItemNS.features, Literal(product['features'])))
        data_graph.add((product_uri, flipItemNS.images, Literal(product['images'])))

        # Brand
        brand_uri = URIRef(f"{BASE_Flipkart}{quote(product['brand']['brand_name'])}")
        data_graph.add((brand_uri, RDF.type, flipItemNS.Producer))
        data_graph.add((brand_uri, flipItemNS.producer_name, Literal(product['brand']['brand_name'])))
        data_graph.add((BASE_Flipkart, flipNS.hasProducer, brand_uri))

        # category and Sub-category
        category_uri = URIRef(f"{BASE_Flipkart}{product['category']['category_name']}")
        data_graph.add((category_uri, RDF.type, flipItemNS.Group))
        data_graph.add((category_uri, flipItemNS.group_name, Literal(product['category']['category_name'])))
        data_graph.add((BASE_Flipkart, flipNS.hasGroup, category_uri))

        sub_category_uri = URIRef(f"{BASE_Flipkart}{product['category']['category_name']}/{product['category']['sub_category']['sub-_category_name']}")
        data_graph.add((sub_category_uri, RDF.type, flipItemNS.SubGroup))
        data_graph.add((sub_category_uri, flipItemNS.sub_group_name, Literal(product['category']['sub_category']['sub-_category_name'])))

        # Product, Brand, Category, sub-category relationships
        data_graph.add((product_uri, flipNS.hasProducer, brand_uri))
        data_graph.add((brand_uri, flipItemNS.producesItem, product_uri))
        data_graph.add((sub_category_uri, flipItemNS.hasItem, product_uri))
        data_graph.add((category_uri, flipItemNS.hasSubGroup, sub_category_uri))
        data_graph.add((category_uri, flipItemNS.hasItem, product_uri))
        data_graph.add((product_uri, flipItemNS.hasGroup, category_uri))

        price_uri = URIRef(f"{BASE_Flipkart}{product['id']}_price")
        data_graph.add((price_uri, RDF.type, flipItemNS.salePrice))
        data_graph.add((price_uri, flipItemNS.salePrice_amount, Literal(str(Decimal(str(product['price']['amount']))), datatype=XSD.decimal)))
        data_graph.add((price_uri, flipItemNS.price_currency, Literal(product['price']['currency'])))
        data_graph.add((product_uri, flipItemNS.hassalePrice, price_uri))

        availability_uri = URIRef(f"{BASE_Flipkart}{product['id']}_availability")
        data_graph.add((availability_uri, RDF.type, flipItemNS.stockStatus))
        data_graph.add((availability_uri, flipItemNS.stockStatus_stock, Literal(product['availability']['stock'])))
        data_graph.add((availability_uri, flipItemNS.stockStatus_status, Literal(product['availability']['status'])))
        data_graph.add((availability_uri, flipItemNS.stockStatus_restock_date, Literal(product['availability']['restock_date'])))
        data_graph.add((product_uri, flipItemNS.hasstockStatus, availability_uri))

        product_return_policy_uri = URIRef(f"{BASE_Flipkart}{product['id']}_return_policy")
        data_graph.add((product_return_policy_uri, RDF.type, flipItemNS.Return_Policy))

        return_period_days = product.get("return_policy", {}).get("return_period_days")
        if return_period_days is not None:
            data_graph.add((product_return_policy_uri,flipItemNS.Return_Rules_return_period_days, Literal(return_period_days)))

        return_conditions = product.get("return_policy", {}).get("conditions")
        if return_conditions is not None:
            data_graph.add((product_return_policy_uri,flipItemNS.Return_Rules_conditions,Literal(return_conditions)))

        data_graph.add((product_return_policy_uri, flipItemNS.Return_Rules_is_return_eligible,  Literal(product['return_policy']['isReturnEligible'])))

        product_return_policy_return_fee_uri = URIRef(f"{BASE_Flipkart}{product['id']}_return_policy/return_fee")
        data_graph.add((product_return_policy_return_fee_uri, RDF.type, flipItemNS.Return_Fee))

        return_fee_price = product.get("return_policy", {}).get("return_fee", {}).get("return_fee_price")
        if return_fee_price is not None:
            data_graph.add((
                product_return_policy_return_fee_uri,
                flipItemNS.return_fee_salePrice,
                Literal(str(Decimal(str(return_fee_price))), datatype=XSD.decimal)
            ))
        return_fee_currency = product.get("return_policy", {}).get("return_fee", {}).get("return_fee_currency")
        if return_fee_currency is not None:
            data_graph.add((
                product_return_policy_return_fee_uri,
                flipItemNS.return_fee_currency,
                Literal(return_fee_currency)
            ))
        data_graph.add((product_return_policy_uri, flipItemNS.hasReturnFee, product_return_policy_return_fee_uri))
        data_graph.add((product_uri, flipItemNS.hasReturnPolicy, product_return_policy_uri))

        # Rating
        product_rating_uri = URIRef(f"{BASE_Flipkart}{product['id']}_rating")
        data_graph.add((product_rating_uri, RDF.type, flipItemNS.hasRating))
        data_graph.add((product_uri, flipItemNS.hasRating, product_rating_uri))
        data_graph.add((product_rating_uri, flipItemNS.rating_average, Literal(str(Decimal(str(product['rating']['rating_average']))), datatype=XSD.decimal)))
        data_graph.add((product_rating_uri, flipItemNS.rating_number_of_reviews, Literal(product['rating']['number_of_reviews'])))

        # Dimensions 
        product_dimensions_uri = URIRef(f"{BASE_Flipkart}{product['id']}_dimensions")
        data_graph.add((product_dimensions_uri, RDF.type, flipItemNS.Dimensions))
        data_graph.add((product_uri, flipItemNS.hasDimensions, product_dimensions_uri))
        data_graph.add((product_dimensions_uri, flipItemNS.dimensions_height_cm, Literal(str(Decimal(str(product['dimensions']['height_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, flipItemNS.dimensions_width_cm, Literal(str(Decimal(str(product['dimensions']['width_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, flipItemNS.dimensions_depth_cm, Literal(str(Decimal(str(product['dimensions']['depth_cm']))), datatype=XSD.decimal)))
        data_graph.add((product_dimensions_uri, flipItemNS.dimensions_weight_cm, Literal(str(Decimal(str(product['dimensions']['weight_kg']))), datatype=XSD.decimal)))

        # Shipping Options
        product_shipping_options_uri = URIRef(f"{BASE_Flipkart}{product['id']}_shipping_options")
        data_graph.add((product_shipping_options_uri, RDF.type, flipItemNS.Shipping_Methods))
        product_shipping_options_uri_price = URIRef(f"{BASE_Flipkart}{product['id']}_shipping_options_price")
        product_shipping_options_uri_delivery = URIRef(f"{BASE_Flipkart}{product['id']}_shipping_options_delivery")
        data_graph.add((product_shipping_options_uri_price, RDF.type, flipItemShippingOptionsNS.salePrice))
        data_graph.add((product_shipping_options_uri_delivery, RDF.type, flipItemShippingOptionsNS.Estimated_Delivery_Time))
        data_graph.add((product_uri, flipItemNS.hasShippingOptions, product_shipping_options_uri))
        data_graph.add((product_shipping_options_uri, flipItemNS.Shipping_Methods_method, Literal(product['shipping_options']['method'])))
        data_graph.add((product_shipping_options_uri, flipItemNS.hasShippingsalePrice, product_shipping_options_uri_price))
        data_graph.add((product_shipping_options_uri, flipItemNS.hasDeliveryTime, product_shipping_options_uri_delivery))
        data_graph.add((product_shipping_options_uri_price, flipItemShippingOptionsNS.Shipping_Methods_salePrice_cost, Literal(str(Decimal(str(product['shipping_options']['price']['cost']))), datatype=XSD.decimal)))
        data_graph.add((product_shipping_options_uri_price, flipItemShippingOptionsNS.Shipping_Methods_salePrice_currency, Literal(product['shipping_options']['price']['currency'])))
        data_graph.add((product_shipping_options_uri_delivery, flipItemShippingOptionsNS.Shipping_Methods_estimated_delivery_time_delivery_time, Literal(product['shipping_options']['estimated_delivery_time']['delivery_time'])))
        data_graph.add((product_shipping_options_uri_delivery, flipItemShippingOptionsNS.Shipping_Methods_estimated_delivery_time_metric, Literal(product['shipping_options']['estimated_delivery_time']['Metric'])))

        # Seller
        seller_uri = URIRef(f"{BASE_Flipkart}seller/{product['seller']['retailer_id']}")
        data_graph.add((seller_uri, RDF.type, flipNS.Seller))
        data_graph.add((product_uri, flipItemNS.hasSeller, seller_uri))
        data_graph.add((seller_uri, flipSellerNS.sells, product_uri))

    # Merge if you want full ontology + data
    full_graph = ontology_graph + data_graph

    # DeductiveClosure(OWLRL_Semantics).expand(full_graph)
    
    # (Optional) serialize and save full_graph
    # full_graph.serialize(destination="full_graph_with_data.ttl", format="turtle")
    full_graph.serialize(destination="full_graph_with_data.ttl", format="turtle")

    return full_graph  # or return full_graph if you want ontology too