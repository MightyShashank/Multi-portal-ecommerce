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
  
export default function Landing_page_top_display_section() {
    
    return (
        <div className="w-full h-12 bg-sky-700 px-20 flex justify-between items-center">
            <div className="text-base font-normal text-white">Welcome to Delta online Multi-portal eCommerce store</div>
            <div className="flex items-center space-x-2 text-white"> {/* items-center vertically makes them centerised*/}
                <div className="text-base font-normal text-white">Follow us:</div>
                <Icon icon="mdi:twitter" width="22" height="22"/>
                <Icon icon="mdi:youtube" width="22" height="22"/>
                <Icon icon="mdi:instagram" width="22" height="22"/>
                <Icon icon="mdi:facebook" width="22" height="22"/>
                <Icon icon="mdi:pinterest" width="22" height="22"/>

                {/* Line in between */}
                <div className="border-l-2 border-sky-600/50 h-7 mx-3"></div>

                {/* Language */}
                <Select>
                    <SelectTrigger className="w-[70px] border-0 [&>span]:text-white [&_svg]:text-white">
                        <SelectValue placeholder="Eng" className="text-white" />
                    </SelectTrigger>
                    <SelectContent>
                        <SelectItem value="english">Eng</SelectItem>
                        <SelectItem value="hindi">हिंदी</SelectItem>
                    </SelectContent>
                </Select>

                {/* Currency */}
                <Select>
                    <SelectTrigger className="w-[70px] border-0 [&>span]:text-white [&_svg]:text-white">
                        <SelectValue placeholder="INR" />
                    </SelectTrigger>
                    <SelectContent>
                        <SelectItem value="inr">INR</SelectItem>
                        <SelectItem value="usd">USD</SelectItem>
                        <SelectItem value="euro">EUR</SelectItem>
                    </SelectContent>
                </Select>
            </div>
        </div>
    )
}
