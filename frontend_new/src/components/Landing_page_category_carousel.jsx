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

const images = [
    {source:"/mobile-removebg-preview.png", name:"Electronics"},
    {source:'/gaming_mouse-removebg-preview.png', name:"Computers and Accesories"},
    {source:'/fridge-removebg-preview.png', name:"Home Appliances"},
    {source:'/fashion_img-removebg-preview.png', name:"Clothing and Fashion"},
    {source:'/perfume_beauty-removebg-preview.png', name:"Beauty and Personal Care"},
    {source:'/book_removebg.jpg', name:"Books"},
    {source:'/toys-removebg-preview.png', name:"Toys and Games"},
    {source:'/sports_cricket-removebg-preview.png', name:"Sports and Outdoors"},
    {source:'/vehicles_removebg.png', name:"Automotive and Vehicles"},
    {source:'/home_furniture.jpg', name:'Home and Furnitures'},
    {source:'/kitchen-removebg-preview.png', name:"Kitchen and Dining"},
    {source:'/grocery-removebg-preview.png', name:"Grocery and Food"},
    {source:'/health_n_wellness_protein-removebg-preview.png', name:"Health and Wellness"},
    {source:'/musical_guitar-removebg-preview.png', name:"Musical Instruments"},
    {source:'/pet_supplies-removebg-preview.png', name:"Pet Supplies"},
    {source:'/office_supplies-removebg-preview.png', name:"Office Supplies"},
    {source:'/arts_n_crafts-removebg-preview.png', name:"Arts and Crafts"},
    {source:'/collectibles_buddha-removebg-preview.png', name:"Collectibles and Memorabilia"},
    {source:'/home_automation-removebg-preview.png', name:"Smart Home"}
  ];

export default function Landing_page_category_carousel() {
    return (
        <div className="w-full px-4 md:px-20 mt-10">
            <div className="pt-6">
                <h2 className="text-2xl font-semibold text-gray-700 mb-4">
                    Shop From <span className="text-sky-600 font-bold">Top Categories</span>
                </h2>
                <div className="mt-2 relative w-full">
                    {/* Grey full line */}
                    <div className="absolute top-0 left-0 w-full h-1 bg-gray-200 rounded" />
                    
                    {/* Blue accent line */}
                    <div className="absolute top-0 left-0 w-72 h-[6px] bg-sky-600 rounded" />
                </div>
            </div>
            <Carousel className="w-full" plugins={[
                Autoplay({
                    delay: 2000,
                }),
            ]}>
                <CarouselContent>
                    {images.map((image, index) => (
                        <CarouselItem key={index} className="basis-1/7 p-4 ml-4 my-10">
                            <div className="w-60 group">
                                <Card className="w-60 h-60 rounded-full overflow-hidden shadow-lg border border-transparent hover:border-blue-400 bg-gray-100 transition-all duration-300 hover:scale-105">
                                    <CardContent className="bg-gray-100 flex items-center justify-center h-full w-full py-0">
                                        <img
                                            src={image.source}
                                            alt={`Product ${index + 1}`}
                                            className="h-full object-contain"
                                        />
                                    </CardContent>
                                </Card>
                                {/* Displaying the name below the image */}
                                <div className="mt-6 text-center text-gray-600 text-lg font-medium group-hover:text-blue-500">
                                    {image.name}
                                </div>
                            </div>
                        </CarouselItem>
                    ))}
                </CarouselContent>
                <CarouselPrevious className="bg-orange-500 text-white border-none hover:bg-orange-600 hover:text-white hover:scale-110" />
                <CarouselNext className="bg-orange-500 text-white border-none hover:bg-orange-600 hover:text-white hover:scale-110"/>
            </Carousel>
        </div>
    );
}
