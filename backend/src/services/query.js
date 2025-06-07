const SPARQL_SERVER = 'http://127.0.0.1:5000/sparql';

// Example query
const query = `
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
        return data;
    } catch (error) {
        console.error('Error executing SPARQL query:', error);
    }
}

