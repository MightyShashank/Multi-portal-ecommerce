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

// Sample product data
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


export default function Landing_page_below_carousel() {
    return (
        <div className="w-full px-20 mt-0">

            <div className="pt-6 mb-16">
                <div className='flex mb-4 space-x-4'>
                    <h2 className="text-2xl font-semibold text-gray-700 items-center">
                        Best <span className="text-sky-600 font-bold">Deals</span>
                    </h2>
                    <CountDownTimer/>
                </div>
                
                <div className="mt-2 relative w-full">
                    {/* Grey full line */}
                    <div className="absolute top-0 left-0 w-full h-1 bg-gray-200 rounded" />
                    
                    {/* Blue accent line */}
                    <div className="absolute top-0 left-0 w-72 h-[6px] bg-sky-600 rounded" />
                </div>
            </div>

            <div className="grid grid-cols-5 grid-rows-2 w-full h-full gap-x-[16px] gap-y-[16px]">

                {/* first div */}
                <div className="col-span-1 row-span-2 bg-gray-100 h-full rounded-sm relative group">

                </div>

                {/* smaller divs */}
                {/* <div className="col-span-1 row-span-2 h-[600px] rounded-md relative group flex flex-col gap-y-4"> */}

                {[...Array(8)].map((_, index) => (
                  <ProductCard productData={productData} key={index} className='col-span-1 row-span-1 bg-gray-100 rounded-sm h-96'/>
                ))}
                {/* </div> */}
            </div>
        </div>
    )
}