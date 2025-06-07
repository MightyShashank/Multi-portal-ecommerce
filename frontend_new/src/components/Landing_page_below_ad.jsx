import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Icon } from "@iconify/react"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import {
    Carousel,
    CarouselContent,
    CarouselItem,
    CarouselNext,
    CarouselPrevious,
} from "@/components/ui/carousel"

import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
import Autoplay from "embla-carousel-autoplay"
import CountDownTimer from '../components/ui/countdowntimer'
import ProductCard from '../components/productCard'

const productData = {
    id: 1,
    title: "Wireless Noise Cancelling Headphones",
    image: "/placeholder.svg?height=300&width=300",
    bestPrice: 149.99,
    bestPlatform: "Amazon",
    platforms: [
      {
        name: "Amazon",
        price: 149.99,
        seller: "AudioTech Official",
        rating: 4.5,
        reviews: 1243,
        returnPolicy: "30 days",
        returnFee: "Free",
        deliveryTime: "2-3 days",
        link: "#",
        stock: 15,
      },
      {
        name: "Flipkart",
        price: 159.99,
        seller: "ElectroHub",
        rating: 4.3,
        reviews: 876,
        returnPolicy: "14 days",
        returnFee: "$5",
        deliveryTime: "3-5 days",
        link: "#",
        stock: 8,
      },
      {
        name: "Myntra",
        price: 164.99,
        seller: "GadgetZone",
        rating: 4.2,
        reviews: 542,
        returnPolicy: "7 days",
        returnFee: "$8",
        deliveryTime: "4-6 days",
        link: "#",
        stock: 0,
      },
    ],
}

export default function Landing_page_below_ad() {

    const tabs = ["All Product", "Keyboard & Mouse", "Headphone", "Webcam", "Printer"];
    const [active, setActive] = useState("All Product");

    return (
        <div className="w-full px-20 mt-14">
            <div className="flex gap-x-[16px]">
                
                <div className="flex flex-col gap-y-2 flex-1 w-full">
                    <div className="text-xl font-semibold text-gray-700 mb-3 flex justify-between">
                        <div className="text-xl font-semibold text-gray-700">Computer Accessories</div>
                        <div className="flex items-center gap-6 text-base font-medium">
                            {tabs.map((tab) => (
                                <button
                                key={tab}
                                onClick={() => setActive(tab)}
                                onMouseEnter={() => setActive(tab)}
                                onMouseLeave={() => setActive(null)}
                                className={`pb-1 transition duration-200 ${
                                    active === tab ? "text-black border-b-2 border-orange-500": "text-gray-500 hover:text-black hover:border-b-2 hover:border-orange-500"
                                }`}
                                >
                                {tab}
                                </button>
                            ))}

                            <div className="ml-auto text-orange-500 hover:underline flex gap-1 cursor-pointer items-center">
                                <span>Browse All Product</span>
                                <span>➜</span>
                            </div>
                        </div>
                    </div>
                    <div className="grid grid-cols-4 grid-rows-2 flex-1 gap-4 w-full">
                        {[...Array(8)].map((_, index) => (
                            <ProductCard productData={productData} key={index} className='col-span-1 row-span-1 bg-gray-100 rounded-sm h-96'/>
                        ))}
                    </div>
                </div>
                <div className="h-[632px]] w-[360px] flex flex-col gap-y-4">
                    <div className="h-8/12 bg-gray-100"> hello1 </div>
                    <div className="h-1/3 bg-gray-100"> hello2 </div>
                </div>
            </div>
        </div>
    )
}

