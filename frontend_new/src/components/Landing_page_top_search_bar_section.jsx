import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../App.css'
import DeltaLogo from '../assets/DeltaLogo.svg'
import { Button } from "@/components/ui/button"
import { Icon } from "@iconify/react";
import SearchBar from '../components/ui/searchbar'


export default function Landing_page_top_search_bar_section() {
    
    return (
        <div className="w-full h-20 pl-20 pr-26 bg-sky-700 flex justify-between items-center border-t-2 border-sky-600/50">
            
            {/* Logo */}
            <a href="/your-target-url" className="group inline-block transition duration-300 hover:bg-[#1a1a1a]/30 rounded-xl p-2">
                <div className="flex justify-between items-center">
                    <img src={DeltaLogo} alt="Logo" className="h-12 w-12" />
                    <div className="text-4xl font-semibold text-white pl-2">DELTA</div>
                </div>
            </a>



            {/* Search bar */}
            <SearchBar width="w-5xl" height="h-12" iconSize={20} borderOptions='border border-white'/>
            
            {/* Icons */}
            <div className="flex items-center space-x-5 text-white"> {/* items-center vertically makes them centerised*/}
                <a href="" className='group inline-block transition duration-300 hover:bg-white/100 rounded-xl p-2 mr-1'>
                    <Icon icon="mdi:cart-outline" width="34" height="34" className='group-hover:text-sky-700 transition-colors duration-300'/>
                </a>
                <a href="" className='group inline-block transition duration-300 hover:bg-white/100 rounded-xl p-2 mr-1'>
                    <Icon icon="mdi:heart-outline" width="34" height="34" className='group-hover:text-sky-700 transition-colors duration-300'/>
                </a>
                <a href="" className='group inline-block transition duration-300 hover:bg-white/100 rounded-xl p-2 mr-1'>
                    <Icon icon="ph:user" width="34" height="34" className='group-hover:text-sky-700 transition-colors duration-300'/>
                </a>
            </div>
        </div>
    )
}