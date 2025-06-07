const SPARQL_SERVER = 'http://127.0.0.1:5000/sparql';

// Example query
const query = `
PREFIX amzNS: <http://delta.org/amazon#>
PREFIX amzProductNS: <http://delta.org/amazon/ProductNS#>

SELECT ?product ?productName ?brand ?price ?categoryName
WHERE {
  ?product a amzNS:Product ;
           amzProductNS:product_name ?productName ;
           amzNS:hasBrand ?brand ;
           amzProductNS:hasPrice/amzProductNS:price_amount ?price ;
           amzProductNS:hasCategory [ amzProductNS:category_name ?categoryName ] .
  
     # Extract source from product URI
  BIND(IF(STRSTARTS(STR(?product), "http://delta.org/amazon"), "Amazon", "Flipkart") AS ?source)
    
  # Brand filter (Apple/Samsung/Sony)
  FILTER(REGEX(STR(?brand), "/(Apple|Samsung|Sony)$", "i"))
  
  # Price range ($200-$800)
  FILTER(?price >= 200 && ?price <= 800)
  
  # Category filter (replace with your target categories)
  FILTER(?categoryName IN ("electronics", "Smartphones", "Laptops")) 
    
    # Source filter (list style - same pattern as category filter)
  FILTER(?source IN ("Amazon"))  # <-- Change this to filter sources
  
  # Quality control
  FILTER(STR(?productName) != "")
}
ORDER BY DESC(?price)
LIMIT 100
`;

// Function to query the Python server
export async function queryGraphDB(SPARQLquery) { // its a named export
    try {
        const response = await fetch(SPARQL_SERVER, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: SPARQLquery }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Query results:', data);
    } catch (error) {
        console.error('Error executing SPARQL query:', error);
    }
}

// Run the query
queryGraphDB(query);
