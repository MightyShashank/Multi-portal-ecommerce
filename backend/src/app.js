const express = require('express');
const app = express();
const cors = require('cors')

const query = require('./services/query');
// lets add our filtering ability
/*
from the FE you are supposed to get: 
  1. A list of platforms
  2. Category
  3. SubCategory
  3. Min Price and Max Price
  4. A list of brands

  Co
*/

app.use(cors()); // allows for requests from frontend
app.use(express.json()); // Parse json bodies, its a middleware


data = {

}

function mergeProducts(products) { // took the products array
  const grouped = {};
  let idCounter = 1;

  for (const item of products) {
    const name = item.productName;

    if (!grouped[name]) {
      grouped[name] = {
        id: item.product,
        title: name,
        image: "/placeholder.svg?height=300&width=300", // You can customize image selection logic
        platforms: [],
      };
    }

    grouped[name].platforms.push({
      name: item.source,
      price: parseFloat(item.price),
      seller: item.seller, // Placeholder, since not available in data
      rating: parseFloat(item.avgRating),
      reviews: parseInt(item.reviewCount),
      returnPolicy: `${item.return_days} days`, // Placeholder
      returnFee: parseFloat(item.return_fee),    // Placeholder
      deliveryTime: "Unknown", // Placeholder
      link: item.product,
      stock: Math.floor(Math.random() * 20), // Simulated stock (optional)
    });
  }

  // Compute bestPrice and bestPlatform for each group
  const merged = Object.values(grouped).map(product => {
    const best = product.platforms.reduce((min, p) => (p.price < min.price ? p : min));
    return {
      ...product,
      bestPrice: best.price,
      bestPlatform: best.name,
    };
  });

  return merged;
}


app.post('/products-api/filter-products', async (req, res) => {

  console.log("req body = ", req.body)
  const { selectedEcommerce, selected, selectedRange, selectedBrands, subCategory } = req.body;

  let selectedBrandsRegexPatters = `"/(${selectedBrands.join('|')})$"`;
  console.log("selectedBrandsRegexPatters = ", selectedBrandsRegexPatters)
  let minValue = selectedRange.minValue ?? 0;
  console.log("minValue = ", minValue);
  let maxValue = selectedRange.maxValue ?? 5000;  
  console.log("maxValue = ", maxValue);
  let formattedCategories = `("${selected}")`;
  console.log("formattedCategories = ", formattedCategories);
  let formattedSubCategories = `(${subCategory.map(item => `"${item}"`).join(', ')})`;
  console.log("formattedSubCategories = ", formattedSubCategories);
  let formattedEcommerce = `(${selectedEcommerce.map(item => `"${item}"`).join(', ')})`;
  console.log("formattedEcommerce = ",formattedEcommerce);

  let subCategoryFilter = 
  formattedSubCategories === 'allProducts'
    ? `# FILTER(?subcategoryName IN ${formattedSubCategories})`
    : `FILTER(?subcategoryName IN ${formattedSubCategories})`;

    console.log("subCategoryFilter = ", subCategoryFilter);
  let ecommerceFilter = 
  formattedEcommerce === 'allEcommerce'
    ? `# FILTER(?source IN ${formattedEcommerce})`
    : `FILTER(?source IN ${formattedEcommerce})`
    console.log("formattedEcommerce = ", formattedEcommerce);

  // now run the sparql queries and get the output
  SPARQL_QUERY = `
  PREFIX amzNS: <http://delta.org/amazon#>
  PREFIX amzProductNS: <http://delta.org/amazon/ProductNS#>

  SELECT ?product ?productName ?brand ?price ?categoryName ?subcategoryName ?source ?avgRating ?reviewCount ?seller ?return_days ?return_fee
  WHERE {
    ?product a amzNS:Product ;
            amzProductNS:product_name ?productName ;
            amzNS:hasBrand ?brand ;
            amzProductNS:hasPrice/amzProductNS:price_amount ?price ;
            amzProductNS:hasCategory [ 
                amzProductNS:category_name ?categoryName ;
                amzProductNS:hasSubCategory [
                  amzProductNS:sub_category_name ?subcategoryName
                ]
            ] ;
            amzProductNS:hasRating [ 
                amzProductNS:rating_average ?avgRating ;
                amzProductNS:rating_number_of_reviews ?reviewCount 
            ] ;
            amzProductNS:hasSeller ?seller ;
            amzProductNS:hasReturnPolicy [
              amzProductNS:return_policy_return_period_days ?return_days ;
              amzProductNS:hasReturnFee [
                amzProductNS:return_fee_price ?return_fee
              ]
            ]
    
    # Source detection
    BIND(IF(STRSTARTS(STR(?product), "http://delta.org/amazon"), "Amazon", "Flipkart") AS ?source)
    
    # All your existing filters (brand, price, etc.) go here
    FILTER(REGEX(STR(?brand), ${selectedBrandsRegexPatters}, "i"))
    FILTER(?price >= ${minValue} && ?price <= ${maxValue})
    FILTER(?categoryName IN ${formattedCategories})
    # FILTER(?subcategoryName IN ${formattedSubCategories})
    ${subCategoryFilter}
    # FILTER(?source IN ${formattedEcommerce})
    ${ecommerceFilter}
    FILTER(STR(?productName) != "")
    
    # Additional rating filters (choose one):
    FILTER(?avgRating >= 0.0)                   # Minimum 4-star products
  }
  ORDER BY DESC(?avgRating)  # Sort by best-rated first
  LIMIT 100
  `;

  console.log(`\n ${SPARQL_QUERY}`)
  products = await query.queryGraphDB(SPARQL_QUERY)
  // console.log('products = ', products)

  const mergedProducts = mergeProducts(products);
  // console.log('merged products = ', JSON.stringify(mergedProducts, null, 2))

  // Then on the given products do some parsing and return an appropriate json
  // Then among all the products see the products across with the same name, then lets send a proper json output

  console.log("Done now sending");
  res.json(mergedProducts);
  console.log("Succesfully sent")
});

app.listen(4000, () => {
  console.log("BE server is running on http://localhost:4000");
});


// 3000 = FE
// 4000 = BE
// 5000 = DB