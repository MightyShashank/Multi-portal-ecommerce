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


export default function Landing_page_ad_display_below_below_category_carousel() {

    return (
        <div className="w-full px-20 mt-14">
            <div className="grid grid-cols-2 grid-rows-1 h-[400px] gap-4">
                <div className="col-span-1 row-span-1 bg-gray-100 rounded-md">ad 1</div>
                <div className="col-span-1 row-span-1 bg-gray-100 rounded-md">ad 2</div>
            </div>
        </div>
    )
}