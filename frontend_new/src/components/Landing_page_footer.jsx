import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../App.css'
import DeltaLogo from '../assets/DeltaLogo.svg'
import { Button } from "@/components/ui/button"
import { Icon } from "@iconify/react";
import SearchBar from '../components/ui/searchbar'
import { Input } from "@/components/ui/input"


const categories = [
    'Computer & Laptop',
    'SmartPhone',
    'Headphone',
    'Accessories',
    'Camera & Photo',
    'TV & Homes'
];

const quick_links = [
    'Shop Product',
    'Shopping Cart',
    'Wishlist',
    'Compare',
    'Track Order',
    'Customer Help',
    'About Us'
];

const popular_tags = [
    'Game', 'iPhone', 'TV', 'Asus Laptops',
    'Macbook', 'SSD', 'Graphics Card',
    'Power Bank', 'Smart TV', 'Speaker',
    'Tablet', 'Microwave', 'Samsung'
];

export default function Landing_page_footer() {
    
    return (
        <div className="w-full mt-20">
            
            {/* first news letter box */}
            <div className="h-[500px] bg-sky-700 border-t-2 border-sky-600/50 flex flex-col gap-y-4 items-center justify-center">
                <div className="text-white flex flex-col gap-y-3 text-center">
                    <div className='text-4xl font-semibold'>Subscribe to our newsletter</div>
                    <div className="text-base text-white/60 font-normal">Subscribe for price drops, top deals, and exclusive savings — all in one place.<br/>Browse across platforms and uncover the best prices before you buy.</div>
                </div>
                <div className="relative w-full max-w-2xl items-center mt-4">
                    <Input
                        type="email"
                        placeholder="Email"
                        className="w-full h-[64px] bg-white text-gray-600 !text-lg placeholder:!text-lg border-none pr-20"
                    />
                    <button
                        type="submit"
                        className="absolute top-1/2 right-2 -translate-y-1/2 h-[48px] bg-orange-500 hover:bg-orange-600 text-white text-lg px-4 flex items-center gap-x-2 rounded-sm"
                    >
                        Subscribe
                        <Icon icon="gridicons:arrow-right" width="20" height="20" />
                    </button>
                </div>

                <div className="border-t-2 border-white/20 w-[600px] mt-6"></div>
                {/* icons */}
                <div className="flex gap-x-8 items-center">
                    <Icon icon="lineicons:amazon" width="80" height="80" style={{color: "#ececec"}} className='mt-2.5 transition-transform duration-300 hover:scale-115 hover:drop-shadow-[0_0_8px_#ececec]'/>
                    <Icon icon="simple-icons:flipkart" width="48" height="48" style={{color: "#ececec"}} className='transition-transform duration-300 hover:scale-115 hover:drop-shadow-[0_0_8px_#ececec]'/>
                    <Icon icon="arcticons:myntra" width="64" height="64" style={{color: "#ececec"}} className='transition-transform duration-300 hover:scale-115 hover:drop-shadow-[0_0_8px_#ececec]'/>
                    <Icon icon="arcticons:meesho" width="64" height="64"  style={{color: "#ececec"}} className='mb-1 transition-transform duration-300 hover:scale-115 hover:drop-shadow-[0_0_8px_#ececec]'/>
                    <Icon icon="simple-icons:aliexpress" width="88" height="88"  style={{color: "#ececec"}} className='mt-2 transition-transform duration-300 hover:scale-115 hover:drop-shadow-[0_0_8px_#ececec]'/>

                </div>
            </div>

            {/* 2nd */}
            <div className="h-[500px] bg-gray-900 flex items-center justify-between px-30 border-b-1 border-gray-400/30">
                <div className="flex flex-col">
                    {/* Logo */}
                    <div className="flex gap-x-1 items-center mb-6">
                        <img src={DeltaLogo} alt="Logo" className='h-12 w-12'></img>
                        <div className="text-4xl font-semibold text-white pl-1 items-center">DELTA</div>
                    </div>
                    {/* Customer Service */}
                    <div className="text-gray-400 text-base">Customer Support</div>
                    <div className="text-white mb-4 text-lg">(+91) 6362437268</div>

                    <div className="text-gray-400 mb-4 text-base">4517 Washington Ave <br/> Manchester, Kentucky 39495</div>
                    <div className="text-white text-lg">info@delta.com</div>
                </div>

                {/* column 2 */}
                <div className="flex flex-col">
                    <div className="text-white mb-4 text-lg">TOP CATEGORY</div>
                    <div className="p-0 w-64 font-sans">
                        <ul className="space-y-2">
                            {categories.map((category, index) => (
                            <li 
                                key={index}
                                className="
                                text-gray-500 
                                px-0
                                py-1 
                                cursor-pointer 
                                transition-colors 
                                duration-200
                                hover:pl-4
                                hover:text-white
                                hover:bg-gray-700
                                relative
                                before:absolute
                                before:left-0
                                before:top-0
                                before:h-full
                                before:w-1
                                before:bg-transparent
                                hover:before:bg-yellow-400
                                "
                            >
                                {category}
                            </li>
                            ))}
                        </ul>
                    </div>
                    <div className="text-yellow-300 mb-4 text-lg flex space-x-4 mt-3 items-center hover:text-xl">
                        Browse All Products 
                        <Icon icon="humbleicons:arrow-right" width="36" height="36"  style={{color: "#c8b600"}} className='pl-2 mt-1 transform-all ease-in-out hover:w-10 hover:h-10'/>
                    </div>
                </div>

                {/* column 3 */}
                <div className="flex flex-col">
                    <div className="text-white mb-4 text-lg">QUICK LINKS</div>
                    <div className="p-0 w-64 font-sans">
                        <ul className="space-y-2">
                            {quick_links.map((category, index) => (
                            <li 
                                key={index}
                                className="
                                text-gray-500 
                                px-0
                                py-1 
                                cursor-pointer 
                                transition-colors 
                                duration-200
                                hover:pl-4
                                hover:text-white
                                hover:bg-gray-700
                                relative
                                before:absolute
                                before:left-0
                                before:top-0
                                before:h-full
                                before:w-1
                                before:bg-transparent
                                hover:before:bg-yellow-400
                                "
                            >
                                {category}
                            </li>
                            ))}
                        </ul>
                    </div>
                </div>

                {/* column 4 */}
                <div className="flex flex-col">
                    <div className="text-white mb-4 text-lg">DOWNLOAD APP</div>
                    <div className="flex flex-col gap-y-4">
                        {/* Google playstore */}
                        <div className="flex space-x-1 bg-gray-700 py-4 px-6 hover:scale-105 hover:bg-gray-500 rounded-sm">
                            <Icon icon="mage:playstore" width="48" height="48"  style={{color: "#fff"}}/>
                            <div className="flex flex-col gap-y-0.5">
                                <div className="text-white text-sm">Get it now</div>
                                <div className="text-white text-lg font-semibold">Google Play</div>
                            </div>
                        </div>
                        {/* App store */}
                        <div className="flex space-x-1 bg-gray-700 py-4 px-6 hover:scale-105 hover:bg-gray-500 rounded-sm">
                            <Icon icon="basil:apple-solid" width="48" height="48"  style={{color: "#fff"}}/>
                            <div className="flex flex-col gap-y-0.5">
                                <div className="text-white text-sm">Get it now</div>
                                <div className="text-white text-lg font-semibold">App Store</div>
                            </div>
                        </div>
                    </div>
                </div>
                
                {/* column 5 */}
                <div className="max-w-md p-6 rounded-lg">
                    <div className="text-white mb-4 text-lg">POPULAR TAGS</div>
                    <div className="flex flex-wrap gap-2">
                        {popular_tags.map((tag, index) => (
                        <span
                            key={index}
                            className="
                            px-3 py-1.5
                            text-white
                            rounded-sm
                            text-sm
                            font-medium
                            border border-gray-600
                            cursor-pointer
                            transition-all
                            duration-200
                            hover:bg-gray-600
                            hover:border-white
                            hover:shadow-sm
                            hover:scale-105
                            "
                        >
                            {tag}
                        </span>
                        ))}
                    </div>
                </div>

            </div>
            
            {/* 3rd */}
            <div className="flex text-gray-500 items-center justify-center bg-gray-900 h-[48px]">Delta Inc. &copy; 2025 All Rights Reserved</div>
        </div>
    )
}