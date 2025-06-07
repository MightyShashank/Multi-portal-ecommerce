"use client"

import { useState } from "react"
import { Star, X, ChevronRight } from "lucide-react"
import { Button } from "./ui/button";

// // Sample product data
// const productData = {
//   id: 1,
//   title: "Wireless Noise Cancelling Headphones",
//   image: "/placeholder.svg?height=300&width=300",
//   bestPrice: 149.99,
//   bestPlatform: "Amazon",
//   platforms: [
//     {
//       name: "Amazon",
//       price: 149.99,
//       seller: "AudioTech Official",
//       rating: 4.5,
//       reviews: 1243,
//       returnPolicy: "30 days",
//       returnFee: "Free",
//       deliveryTime: "2-3 days",
//       link: "#",
//       stock: 15,
//     },
//     {
//       name: "Flipkart",
//       price: 159.99,
//       seller: "ElectroHub",
//       rating: 4.3,
//       reviews: 876,
//       returnPolicy: "14 days",
//       returnFee: "$5",
//       deliveryTime: "3-5 days",
//       link: "#",
//       stock: 8,
//     },
//     {
//       name: "Myntra",
//       price: 164.99,
//       seller: "GadgetZone",
//       rating: 4.2,
//       reviews: 542,
//       returnPolicy: "7 days",
//       returnFee: "$8",
//       deliveryTime: "4-6 days",
//       link: "#",
//       stock: 0,
//     },
//   ],
// }

const bestPlatformRating = (productData) => {
    const rating = productData.platforms.find(
        (p) => p.name === productData.bestPlatform
      )?.rating;
    return rating;
}

const bestPlatformReviews = (productData) => {
    const reviews = productData.platforms.find(
        (p) => p.name === productData.bestPlatform
      )?.reviews;
    return reviews;
}

const ProductCard = ({productData}) => {
  const [isExpanded, setIsExpanded] = useState(false)
  const [hoveredPlatform, setHoveredPlatform] = useState(null)
  const [quantities, setQuantities] = useState(
    productData.platforms.reduce((acc, platform) => {
      acc[platform.name] = 1
      return acc
    }, {}),
  )

  const toggleExpand = () => {
    setIsExpanded(!isExpanded)
  }

  const handlePlatformHover = (platform) => {
    setHoveredPlatform(platform)
  }

  const handlePlatformLeave = () => {
    setHoveredPlatform(null)
  }

//   const handleAddToCart = () => {
//     setQuantity(quantity + 1);
//   };

//   const increaseQuantity = () => {
//     setQuantity(quantity + 1);
//   };

  const handleQuantityChange = (platform, value) => {
    const newValue = Number.parseInt(value)
    if (isNaN(newValue) || newValue < 1) return

    // Ensure quantity doesn't exceed available stock
    const maxStock = platform.stock
    const validValue = Math.min(newValue, maxStock)

    setQuantities({
      ...quantities,
      [platform.name]: validValue,
    })
  }

  // Render stars based on rating
  const renderStars = (rating, size=4) => {
    const stars = []
    const fullStars = Math.floor(rating)
    const hasHalfStar = rating % 1 >= 0.5

    
    for (let i = 0; i < fullStars; i++) {
      stars.push(<Star key={`full-${i}`} className={`w-${size} h-${size} fill-orange-400 text-orange-400`} />)
    }

    if (hasHalfStar) {
      stars.push(
        <div key="half" className="relative">
          <Star className={`w-${size} h-${size} text-gray-300`} />
          <div className="absolute top-0 left-0 overflow-hidden w-1/2">
            <Star className={`w-${size} h-${size} fill-orange-400 text-orange-400`} />
          </div>
        </div>,
      )
    }

    const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0)
    for (let i = 0; i < emptyStars; i++) {
      stars.push(<Star key={`empty-${i}`} className={`w-${size} h-${size} text-gray-300`} />)
    }

    return stars
  }

  if (isExpanded) {
    return (
      <div className="fixed inset-0 bg-white z-50 overflow-auto p-4 md:p-8">
        <div className="max-w-[1800px] mx-auto">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold text-gray-800">{productData.title}</h2>
            <button onClick={toggleExpand} className="p-2 rounded-full hover:bg-gray-100">
              <X className="w-6 h-6 text-gray-600" />
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
            <div className="bg-gray-50 rounded-lg p-6 flex items-center justify-center">
              <img
                src={productData.image || "/placeholder.svg"}
                alt={productData.title}
                className="max-h-80 object-contain"
              />
            </div>
            <div>
              <div className="mb-6">
                <h3 className="text-xl font-semibold text-gray-800 mb-2">Best Deal</h3>
                <div className="flex items-center">
                  <span className="text-3xl font-bold text-blue-600">${productData.bestPrice}</span>
                  <span className="ml-2 px-2 py-1 bg-orange-100 text-orange-600 text-sm font-medium rounded">
                    Best Price
                  </span>
                </div>
                <p className="text-gray-600 mt-2">on {productData.bestPlatform}</p>
              </div>

              <div className="space-y-4">
                <h3 className="text-lg font-semibold text-gray-800">Product Details</h3>
                <p className="text-gray-600">
                  Experience premium sound quality with these wireless noise-cancelling headphones. Perfect for music
                  lovers and professionals alike, these headphones deliver crystal-clear audio and exceptional comfort
                  for extended use.
                </p>
                <div className="flex space-x-2">
                  <span className="px-2 py-1 bg-gray-100 text-gray-600 text-sm rounded">Wireless</span>
                  <span className="px-2 py-1 bg-gray-100 text-gray-600 text-sm rounded">Noise Cancelling</span>
                  <span className="px-2 py-1 bg-gray-100 text-gray-600 text-sm rounded">Bluetooth 5.0</span>
                </div>
              </div>
            </div>
          </div>
          
          <div className="mb-8">
            <h3 className="text-xl font-semibold text-gray-800 mb-4">Price Comparison</h3>
            <div className="overflow-x-auto">
              <table className="w-full border-collapse">
                <thead>
                  <tr className="bg-gray-50">
                    <th className="py-3 px-4 text-left text-gray-600 font-semibold">Platform</th>
                    <th className="py-3 px-4 text-left text-gray-600 font-semibold">Price</th>
                    <th className="py-3 px-4 text-left text-gray-600 font-semibold">Seller</th>
                    <th className="py-3 px-4 text-left text-gray-600 font-semibold">Rating</th>
                    <th className="py-3 px-4 text-left text-gray-600 font-semibold">Return Policy</th>
                    <th className="py-3 px-4 text-left text-gray-600 font-semibold">Delivery</th>
                    <th className="py-3 px-4 text-left text-gray-600 font-semibold">Stock</th>
                    <th className="py-3 px-4 text-left text-gray-600 font-semibold">Quantity</th>
                    <th className="py-3 px-4 text-left text-gray-600 font-semibold"></th>
                  </tr>
                </thead>
                <tbody>
                  {productData.platforms.map((platform, index) => (
                    <tr
                      key={platform.name}
                      className={`border-b ${platform.price === productData.bestPrice ? "bg-blue-50" : ""}`}
                    >
                      <td className="py-4 px-4">
                        <div className="font-medium text-gray-800">{platform.name}</div>
                      </td>
                      <td className="py-4 px-4">
                        <div className="font-bold text-gray-800">
                          ${platform.price}
                          {platform.price === productData.bestPrice && (
                            <span className="ml-2 px-2 py-0.5 bg-orange-100 text-orange-600 text-xs font-medium rounded">
                              Best
                            </span>
                          )}
                        </div>
                      </td>
                      <td className="py-4 px-4">
                        <div className="text-gray-600">{platform.seller}</div>
                      </td>
                      <td className="py-4 px-4">
                        <div className="flex items-center">
                          <div className="flex mr-1">{renderStars(platform.rating)}</div>
                          <span className="text-sm text-gray-500">({platform.reviews})</span>
                        </div>
                      </td>
                      <td className="py-4 px-4">
                        <div className="text-gray-600">{platform.returnPolicy.split(' ').slice(0, 2).join(' ')}<br />
                        {platform.returnPolicy.split(' ').slice(2).join(' ')}</div>
                        <div className="text-sm text-gray-500">Return fee: {platform.returnFee}</div>
                      </td>
                      <td className="py-4 px-4">
                        <div className="text-gray-600">{platform.deliveryTime}</div>
                      </td>
                      <td className="py-4 px-4">
                        <div
                          className={`text-sm font-medium ${platform.stock > 0 ? "text-green-600" : "text-red-600"}`}
                        >
                          {platform.stock > 0 ? `In Stock (${platform.stock})` : "Out of Stock"}
                        </div>
                      </td>
                      <td className="py-4 px-4">
                        <div className="flex items-center">
                          <input
                            type="number"
                            min="1"
                            max={platform.stock}
                            value={quantities[platform.name]}
                            onChange={(e) => handleQuantityChange(platform, e.target.value)}
                            disabled={platform.stock === 0}
                            className="w-16 p-1 border rounded text-center disabled:bg-gray-100 disabled:text-gray-400"
                          />
                        </div>
                      </td>
                      <td className="py-4 px-4">
                        <button
                          onClick={(e) => {
                            e.stopPropagation()
                            alert(`Added ${quantities[platform.name]} item(s) from ${platform.name} to cart`)
                          }}
                          disabled={platform.stock === 0}
                          className={`inline-flex items-center px-3 py-1.5 text-sm font-medium rounded ${
                            platform.stock > 0
                              ? "bg-blue-600 text-white hover:bg-blue-700"
                              : "bg-gray-300 text-gray-500 cursor-not-allowed"
                          }`}
                        >
                          Add to Cart
                          {platform.stock > 0 ? <ChevronRight className="w-4 h-4 ml-1" /> : null}
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div className="border rounded-lg p-4">
              <h4 className="font-medium text-gray-800 mb-2">Shipping Information</h4>
              <p className="text-gray-600 text-sm">
                Shipping times vary by platform. Amazon offers the fastest delivery with their Prime service. All
                platforms provide tracking information once the order is shipped.
              </p>
            </div>
            <div className="border rounded-lg p-4">
              <h4 className="font-medium text-gray-800 mb-2">Return Policies</h4>
              <p className="text-gray-600 text-sm">
                Amazon offers the most generous return policy with 30 days and free returns. Make sure to check the
                condition requirements for returns on each platform.
              </p>
            </div>
            <div className="border rounded-lg p-4">
              <h4 className="font-medium text-gray-800 mb-2">Price History</h4>
              <p className="text-gray-600 text-sm">
                The current price on Amazon is the lowest in the past 30 days. Prices typically drop during holiday
                sales and special promotions.
              </p>
            </div>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="w-full rounded-lg overflow-hidden shadow-md hover:shadow-lg transition-shadow duration-300 bg-white cursor-pointer" onClick={toggleExpand}>

      {/* Image */}
      <div className="relative">
        <img src={productData.image || "/placeholder.svg"} alt={productData.title} className="w-full h-56 object-contain bg-gray-50 p-4"/>
      </div>

      {/* Rating */}
      <div className="flex items-center p-2">
          <div className="flex mr-1">{renderStars(bestPlatformRating(productData), 5)}</div>
          <span className="text-lg text-gray-500">({bestPlatformReviews(productData)})</span>
      </div>

      {/* title  */}
      <div className="p-0">
        <h3 className="text-gray-800 font-medium text-base mb-2 line-clamp-2 h-10 pl-2">{productData.title}</h3>
        <div className="flex justify-between items-center mb-5">
          <div>
            <p className="text-blue-600 font-bold text-lg pl-2">${productData.bestPrice}</p>
            <p className="text-medium text-gray-500 pl-2">on {productData.bestPlatform}</p>
          </div>
        </div>
      </div>

    </div>
  )
}

export default ProductCard
