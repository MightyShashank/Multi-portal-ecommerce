import { useState } from 'react'
import "../App.css"
import { useNavigate } from 'react-router-dom'
import Landing_page_top_display_section from '../components/Landing_page_top_display_section'
import Landing_page_top_search_bar_section from '../components/Landing_page_top_search_bar_section'
import Landing_page_top_below_search_bar_section from '../components/Landing_page_top_below_search_bar_section'
import Landing_page_carousel from '../components/Landing_page_carousel'
import Landing_page_footer from '@/components/Landing_page_footer'
import Landing_page_category_carousel from '../components/Landing_page_category_carousel'
import Landing_page_below_carousel from '../components/Landing_page_below_carousel'
import Landing_page_below_category_carousel from '../components/Landing_page_below_category_carousel'
import Landing_page_ad_display_below_below_category_carousel from '../components/Landing_page_ad_display_below_below_category_carousel'
import Landing_page_below_ad from '../components/Landing_page_below_ad'
import Product_page_with_category from '../components/product_page_with_category'

export default function Product_Page() {

    return (
        <div className="">

            {/* Header */}
            <Landing_page_top_display_section/>
            <Landing_page_top_search_bar_section/>
            <Landing_page_top_below_search_bar_section/>

            <Product_page_with_category/>

            {/* Footer */}
            <Landing_page_footer/>
        </div>
    )
}