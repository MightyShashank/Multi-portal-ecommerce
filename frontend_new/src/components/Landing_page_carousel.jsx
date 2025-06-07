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

  
export default function Landing_page_carousel() {
    
    return (
        <div className="w-full px-20 flex justify-between items-center h-[600px] mt-4">
        
            <div className="grid grid-cols-5 grid-rows-2 w-full h-full gap-x-[16px] gap-y-[16px]">

                {/* first div */}
                <div className="col-span-3 row-span-2 bg-white h-[600px] rounded-md relative group">
                    <Carousel className="w-full" plugins={[
                        Autoplay({
                        delay: 2000,
                        }),
                    ]}
                    style={{ overflow: 'visible' }}
                    >
                        <CarouselContent className="rounded-md">
                            {Array.from({ length: 5 }).map((_, index) => (
                            <CarouselItem key={index} className="pl-0 bg-gray-100 rounded-md">
                                <div className="p-0 rounded-md">
                                <Card className="p-0 border-none bg-gray-100 rounded-md">
                                    <CardContent className="flex items-center justify-center p-0 rounded-md">
                                    <span className="text-4xl font-semibold h-[600px]">{index + 1}</span>
                                    </CardContent>
                                </Card>
                                </div>
                            </CarouselItem>
                            ))}
                        </CarouselContent>
                        <CarouselPrevious className="absolute left-4 top-1/2 -translate-y-1/2 z-10 opacity-0 group-hover:opacity-100 transition-opacity" />
                        <CarouselNext className="absolute right-4 top-1/2 -translate-y-1/2 z-10 opacity-0 group-hover:opacity-100 transition-opacity" />
                    </Carousel>
                </div>

                {/* second div */}
                <div className="flex flex-col col-span-2 row-span-2 gap-y-4 rounded-md">
                    <div className="col-span-2 row-span-1 bg-gray-100 h-full w-full p-4 flex items-center">
                        <img
                            src="/xiaomi_buds.png" // Replace with actual image path
                            alt="Xiaomi FlipBuds Pro"
                            className="w-28 h-28 object-contain"
                        />
                        <div className="ml-4">
                            <h2 className="text-lg font-semibold text-gray-800">Xiaomi FlipBuds Pro</h2>
                            <p className="text-blue-500 font-medium mt-1">$299 USD</p>
                            <button className="mt-4 bg-orange-500 hover:bg-orange-600 text-white px-4 py-2 text-sm rounded-md flex items-center">
                                SHOP NOW <span className="ml-2">→</span>
                            </button>
                        </div>
                    </div>

                    {/* third div */}
                    <div className="col-span-2 row-span-1 bg-gray-100 h-full w-full rounded-md">
                        Hello3
                    </div>
                </div>
                
            </div>

        </div>
    )
}
