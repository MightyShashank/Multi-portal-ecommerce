import { useEffect, useState } from 'react';
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
import CountDownTimer from './ui/countdowntimer'
import SearchBar from './ui/searchbar'
import * as React from "react"
import { Check, ChevronsUpDown } from "lucide-react"
 
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Input } from "@/components/ui/input"

import {
    Breadcrumb,
    BreadcrumbEllipsis,
    BreadcrumbItem,
    BreadcrumbLink,
    BreadcrumbList,
    BreadcrumbPage,
    BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Link } from 'react-router-dom';
import ProductCard from '../components/productCard'

const optionsList = [
    {
      value: "mostPopular",
      label: "Most Popular",
    },
    {
      value: "priceLowToHigh",
      label: "Price Low to High",
    },
    {
      value: "priceHighToLow",
      label: "Price High to Low",
    },
]

export function BreadcrumbDemo() {
    return (
      <Breadcrumb>
        <BreadcrumbList>

          <BreadcrumbItem>
            <BreadcrumbLink asChild>
              <Link to="/">Home</Link>
            </BreadcrumbLink>
          </BreadcrumbItem>
  
          <BreadcrumbSeparator />
  
          <BreadcrumbItem>
            <BreadcrumbLink asChild>
              <Link to="/product_page">Product Page</Link>
            </BreadcrumbLink>
          </BreadcrumbItem>

        </BreadcrumbList>
      </Breadcrumb>
    );
}

export function ComboboxDemo() {
    const [open, setOpen] = React.useState(false)
    const [value, setValue] = React.useState("")
   
    return (
      <Popover open={open} onOpenChange={setOpen}>
        <PopoverTrigger asChild>
          <Button
            variant="outline"
            role="combobox"
            aria-expanded={open}
            className="w-[200px] justify-between border-2 border-gray-200/40 h-12"
          >
            {value
              ? optionsList.find((framework) => framework.value === value)?.label
              : "Filter"}
            <ChevronsUpDown className="opacity-50" />
          </Button>
        </PopoverTrigger>
        <PopoverContent className="w-[200px] p-0">
          <Command>
            <CommandInput placeholder="Search filter..." className="h-9" />
            <CommandList>
              <CommandEmpty>No filter found.</CommandEmpty>
              <CommandGroup>
                {optionsList.map((framework) => (
                  <CommandItem
                    key={framework.value}
                    value={framework.value}
                    onSelect={(currentValue) => {
                      setValue(currentValue === value ? "" : currentValue)
                      setOpen(false)
                    }}
                  >
                    {framework.label}
                    <Check
                      className={cn(
                        "ml-auto",
                        value === framework.value ? "opacity-100" : "opacity-0"
                      )}
                    />
                  </CommandItem>
                ))}
              </CommandGroup>
            </CommandList>
          </Command>
        </PopoverContent>
      </Popover>
    )
}

const categories  = [
    { id: "r0", value: "allProducts", label: "All Products" },
    { id: "r1", value: "electronics", label: "Electronics" },
    { id: "r2", value: "computers-accessories", label: "Computers and Accessories" },
    { id: "r3", value: "home-appliances", label: "Home Appliances" },
    { id: "r4", value: "fashion", label: "Clothing and Fashion" },
    { id: "r5", value: "beauty-personal-care", label: "Beauty and Personal care" },
    { id: "r6", value: "books-stationery", label: "Books and Stationery" },
    { id: "r7", value: "toys-games", label: "Toys and Games" },
    { id: "r8", value: "sports-outdoors", label: "Sports and Outdoors" },
    { id: "r9", value: "automotive-vehicles", label: "Automotive and Vehicles" },
    { id: "r10", value: "home-furniture", label: "Home and Furniture" },
    { id: "r11", value: "kitchen-dining", label: "Kitchen and Dining" },
    { id: "r12", value: "grocery-food", label: "Grocery and Food" },
    { id: "r13", value: "health-wellness", label: "Health and Wellness" },
    { id: "r14", value: "musical-instruments", label: "Musical Instruments" },
    { id: "r15", value: "pet-supplies", label: "Pet Supplies" },
    { id: "r16", value: "industry-scientific", label: "Industry and Scientific" },
    { id: "r17", value: "office-business-supplies", label: "Office and Business Supplies" },
    { id: "r18", value: "arts-crafts", label: "Arts and Crafts" },
    { id: "r19", value: "collectibles-memorabilia", label: "Collectibles and Memorabilia" },
    { id: "r20", value: "smart-home-automation", label: "Smart Home and Automation" }
];

const priceRanges = [
    { id: "p1", label: "All Price", minValue: null, maxValue: null },
    { id: "p2", label: "Under $20", minValue: null, maxValue: 20 },
    { id: "p3", label: "$25 to $100", minValue: 25, maxValue: 100 },
    { id: "p4", label: "$100 to $300", minValue: 100, maxValue: 300 },
    { id: "p5", label: "$300 to $500", minValue: 300, maxValue: 500 },
    { id: "p6", label: "$500 to $1,000", minValue: 500, maxValue: 1000 },
    { id: "p7", label: "$1,000 to $10,000", minValue: 1000, maxValue: 10000 },
];



const popularBrands = {
    "electronics": [
        { id: "be1", label: "Apple", value: "Apple"},
        { id: "be2", label: "Samsung", value: "Samsung"},
        { id: "be3", label: "Google", value: "Google"},
        { id: "be4", label: "OnePlus", value: "OnePlus"},
        { id: "be5", label: "Sony", value: "Sony"},
        { id: "be6", label: "Xiaomi", value: "Xiaomi"},
        { id: "be7", label: "Oppo", value: "Oppo"},
        { id: "be8", label: "Vivo", value: "Vivo"},
        { id: "be9", label: "Asus", value: "Asus"},
        { id: "be10", label: "Realme", value: "Realme"},
    ],
    "fashion": [
        { id: "bf1", label: "Zara", value: "Zara"},
        { id: "bf2", label: "Adidas", value: "Adidas"},
        { id: "bf3", label: "Nike", value: "Nike"},
        { id: "bf4", label: "Mango", value: "Mango"},
        { id: "bf5", label: "Uniqlo", value: "Uniqlo"},
        { id: "bf6", label: "Columbia", value: "Columbia"},
        { id: "bf7", label: "Gap", value: "Gap"},
        { id: "bf8", label: "H&M", value: "H&M"},
        { id: "bf9", label: "Coach", value: "Coach"},
        { id: "bf10", label: "Rolex", value: "Rolex"},
    ]
}

const ecommerceOptions =  [
    { id: "amz", label: "Amazon", value: "Amazon"},
    { id: "flip", label: "Flipkart", value: "Flipkart"},
    { id: "myn", label: "Myntra", value: "Myntra"},
]
  
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

export function EcommerceGroup({selectedEcommerce, setselectedEcommerce}) {
    
    const handleBrandToggle = (brandValue) => {
        setselectedEcommerce(prev => 
          prev.includes(brandValue) ? prev.filter(b => b !== brandValue) : [...prev, brandValue]
        );
    };

    return (
      <div className="items-start text-left">
        <h2 className="text-xl font-semibold uppercase mb-4 tracking-wide">Platform</h2>
        <div className="space-y-2">
            {ecommerceOptions.map((brand) => (
              <div key={brand.id} className="flex items-center">
                <input 
                  type="checkbox" 
                  id={brand.id} 
                  checked={selectedEcommerce.includes(brand.value)} 
                  onChange={() => handleBrandToggle(brand.value)} 
                  className="h-4 w-4 appearance-none rounded border border-gray-300 bg-white checked:bg-orange-500 checked:border-orange-500 focus:ring-orange-500 focus:ring-offset-0"
                />
                <label htmlFor={brand.id} className="ml-2 text-gray-700">
                  {brand.label}
                </label>
              </div>
            ))}
        </div>
      </div>
    );
}

export function CategoryRadioGroup({selected, setSelected}) {
  
    return (
      <div className="items-start text-left">
        <h2 className="text-xl font-semibold uppercase mb-4 tracking-wide">Category</h2>
        <div className="space-y-2">
          {categories.map((cat) => (
            <label key={cat.id} className="flex items-center space-x-2 cursor-pointer">
              <input type="radio" name="category" value={cat.value} checked={selected === cat.value} onChange={() => setSelected(cat.value)} className="peer hidden"/>
              <span className="w-4 h-4 rounded-full border-2 peer-checked:border-[5px] border-gray-400 peer-checked:border-orange-500 flex items-center justify-center transition-all duration-150">
                <span className="w-2 h-2 bg-orange-500 rounded-full peer-checked:opacity-100 opacity-0 transition-opacity duration-150" />
              </span>

              <span className={`text-base ${selected === cat.value ? "font-semibold text-black" : "text-gray-700"}`}>{cat.label}</span>
            </label>
          ))}
        </div>
      </div>
    );
}

export function PriceRange({selectedRange, setSelectedRange}) {
  
    const isSelected = (range) =>
      selectedRange.minValue === range.minValue && selectedRange.maxValue === range.maxValue;
  
    return (
      <div className="items-start text-left flex flex-col space-y-2 w-full">
        <h2 className="text-xl font-semibold uppercase mb-4 tracking-wide">Price</h2>
  
        <div className="flex space-x-2 w-full">
          <Input placeholder="Min price" type="number" />
          <Input placeholder="Max price" type="number" />
        </div>
  
        <div className="space-y-2 mt-2">
          {priceRanges.map((range) => (
            <label key={range.id} className="flex items-center space-x-2 cursor-pointer">
              <input
                type="radio"
                name="price"
                className="peer hidden"
                checked={isSelected(range)}
                onChange={() => setSelectedRange({ minValue: range.minValue, maxValue: range.maxValue })}
              />
              <span className="w-4 h-4 rounded-full border-2 peer-checked:border-[5px] border-gray-400 peer-checked:border-orange-500 flex items-center justify-center transition-all duration-150">
                <span className="w-2 h-2 bg-orange-500 rounded-full peer-checked:opacity-100 opacity-0 transition-opacity duration-150" />
              </span>
              <span
                className={`text-base ${
                  isSelected(range) ? "font-semibold text-black" : "text-gray-700"
                }`}
              >
                {range.label}
              </span>
            </label>
          ))}
        </div>
      </div>
    );
}


export function PopularBrandsChecklist({selectedBrands, setSelectedBrands, selected}) {
  
    const handleBrandToggle = (brandValue) => {
      setSelectedBrands(prev => 
        prev.includes(brandValue) 
          ? prev.filter(b => b !== brandValue) 
          : [...prev, brandValue]
      );
    };
  
    return (
      <div className="items-start text-left w-full">
        <h2 className="text-xl font-semibold mb-4">POPULAR BRANDS</h2>
        <div className="grid grid-cols-2 gap-4">
          <div className="space-y-2">
            {popularBrands[selected].slice(0, Math.ceil(popularBrands[selected].length / 2)).map((brand) => (
              <div key={brand.id} className="flex items-center">
                <input 
                  type="checkbox" 
                  id={brand.id} 
                  checked={selectedBrands.includes(brand.value)} 
                  onChange={() => handleBrandToggle(brand.value)} 
                  className="h-4 w-4 appearance-none rounded border border-gray-300 bg-white checked:bg-orange-500 checked:border-orange-500 focus:ring-orange-500 focus:ring-offset-0"
                />
                <label htmlFor={brand.id} className="ml-2 text-gray-700">
                  {brand.label}
                </label>
              </div>
            ))}
          </div>
          <div className="space-y-2">
            {popularBrands[selected].slice(Math.ceil(popularBrands[selected].length / 2)).map((brand) => (
              <div key={brand.id} className="flex items-center">
                <input 
                  type="checkbox" 
                  id={brand.id} 
                  checked={selectedBrands.includes(brand.value)} 
                  onChange={() => handleBrandToggle(brand.value)} 
                  className="h-4 w-4 appearance-none rounded border border-gray-300 bg-white checked:bg-orange-500 checked:border-orange-500 focus:ring-orange-500 focus:ring-offset-0"
                />
                <label htmlFor={brand.id} className="ml-2 text-gray-700">
                  {brand.label}
                </label>
              </div>
            ))}
          </div>
        </div>
      </div>
    );
}


const subCategories = {
    "electronics": [
        { id: "sce1", label: "Smartphones", value: "smartphones"},
        { id: "sce2", label: "Laptops", value: "laptops"},
        { id: "sce3", label: "Tablets", value: "tablets"},
        { id: "sce4", label: "Smartwatches", value: "smartwatches"},
        { id: "sce5", label: "Headphones", value: "headphones"},
        { id: "sce6", label: "Cameras", value: "cameras"},
        { id: "sce7", label: "Gaming Consoles", value: "gaming-consoles"},
        { id: "sce8", label: "Drones", value: "drones"},
        { id: "sce9", label: "Power Banks", value: "power-banks"},
        { id: "sce10", label: "Smart Home", value: "smart-home"},
    ],
    "fashion": [
        { id: "scf1", label: "Mens Clothing", value: "mens-clothing"},
        { id: "scf2", label: "Womens Clothing", value: "womens-clothing"},
        { id: "scf3", label: "Kids Clothing", value: "kids-clothing"},
        { id: "scf4", label: "Footwear", value: "footwear"},
        { id: "scf5", label: "Bags and Backpacks", value: "bags-backpacks"},
        { id: "scf6", label: "Watches", value: "watches"},
        { id: "scf7", label: "Sunglasses", value: "sunglasses"},
        { id: "scf8", label: "Hats and Caps", value: "hats-caps"},
        { id: "scf9", label: "Jewelry", value: "jewelry"},
        { id: "scf10", label: "Sportswear", value: "sportswear"},
    ], 
    "home-appliances": [
        { id: "sch1", label: "Refrigerators", value: "refrigerators"},
        { id: "sch2", label: "Washing Machines", value: "washing-machines"},
        { id: "sch3", label: "Air Conditionersg", value: "air-conditioners"},
        { id: "sch4", label: "Vacuum Cleaners", value: "vacuum-cleaners"},
        { id: "sch5", label: "Microwaves", value: "microwaves"},
        { id: "sch6", label: "Coffee Makers", value: "coffee-makers"},
        { id: "sch7", label: "Dishwashers", value: "dishwashers"},
        { id: "sch8", label: "Water Purifiers", value: "water-purifiers"},
        { id: "sch9", label: "Air Purifiers", value: "air-purifiers"},
        { id: "sch10", label: "Induction Cooktops", value: "induction-cooktops"},
    ]
}

export function PopularTags({ subCategory, setSubCategory, selected }) {

    function handleSubCatOnClick(value) {
      if (subCategory.includes(value)) {
        // Deselect: remove from list
        setSubCategory(subCategory.filter((v) => v !== value));
        console.log(subCategory);
      } else {
        // Select: add to list
        setSubCategory([...subCategory, value]);
        console.log(subCategory);
      }
    }
  
    return (
      <div className="items-start text-left">
        <h2 className="text-xl font-semibold uppercase mb-4 tracking-wide">POPULAR TAG</h2>
        <div className="flex flex-wrap gap-2">
          {subCategories[selected].map((subcat) => (
            <button
              key={subcat.id}
              className={`px-3 py-1 border rounded-md text-sm ${
                subCategory.includes(subcat.value)
                  ? "bg-orange-200 border-orange-600 text-orange"
                  : "bg-white border-gray-300 text-gray-800"
              }`}
              onClick={() => handleSubCatOnClick(subcat.value)}
            >
              {subcat.label}
            </button>
          ))}
        </div>
      </div>
    );
  }
  
import { useDataset } from '../DatasetContext.jsx';

export default function Product_page_with_category() {

    const [selectedEcommerce, setselectedEcommerce] = useState(['Amazon']);
    const [selected, setSelected] = useState("electronics");
    const [selectedRange, setSelectedRange] = useState({ minValue: null, maxValue: null });
    const [selectedBrands, setSelectedBrands] = useState(['OnePlus', 'Apple', 'Oppo']);
    const [subCategory, setSubCategory] = useState([`${subCategories[selected][0].value}`]);

    let Dataset = []

    function FilteredProductsComponent() {
        const { setDataset } = useDataset();
      
        useEffect(() => {
          const sendFiltersToBackend = async () => {
            const filters = { selectedEcommerce, selected, selectedRange, selectedBrands, subCategory };
      
            try {
              const response = await fetch('http://localhost:4000/products-api/filter-products', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(filters)
              });
      
              const products = await response.json();
              console.log('Received products:', products);
              setDataset(products); // ✅ updates context
            } catch (error) {
              console.error("Error: ", error);
            }
          };
      
          sendFiltersToBackend();
        }, [selectedEcommerce, selected, selectedRange, selectedBrands, subCategory]);
    }
    
    FilteredProductsComponent();

    const {dataset} = useDataset();
    return (
        <div className="flex flex-col mb-5">
            <div className="h-16 mb-5 px-20 bg-gray-200/50 flex items-center"><BreadcrumbDemo/></div>
            <div className="w-full px-20 mt-4 flex flex-col">
                <div className="flex gap-x-[16px]"> {/* the display section*/}
                    {/* Left side bar */}
                    <div className="h-full bg-white w-[360px] flex flex-col items-start text-left gap-y-4">
                        <EcommerceGroup selectedEcommerce={selectedEcommerce} setselectedEcommerce={setselectedEcommerce}/>
                        <div className="bg-gray-100 h-0.5 mt-2 w-full"></div>
                        <CategoryRadioGroup selected={selected} setSelected={setSelected}/>
                        <div className="bg-gray-100 h-0.5 mt-2 w-full"></div>
                        <PriceRange selectedRange={selectedRange} setSelectedRange={setSelectedRange}/>
                        <div className="bg-gray-100 h-0.5 mt-2 w-full"></div>
                        <PopularBrandsChecklist selectedBrands={selectedBrands} setSelectedBrands={setSelectedBrands} selected={selected}/>
                        <div className="bg-gray-100 h-0.5 mt-2 w-full"></div>
                        <PopularTags subCategory={subCategory} setSubCategory={setSubCategory} selected={selected}/>
                    </div>
                    
                    <div className="flex flex-col gap-y-2 flex-1 w-full">
                        <div className="text-base font-semibold text-gray-700 flex justify-between items-center">
                            <SearchBar width="w-xl" height="h-12" iconSize={16} borderOptions='border-2 border-gray-200/40'/>
                            <div className="flex gap-x-4 items-center">
                                <div className="text-base">Sort by:</div>
                                <ComboboxDemo/>
                            </div>
                        </div>
                        <div className="h-12 w-full bg-gray-200/50 rounded-sm mb-2"></div>
                        <div className="grid grid-cols-4 grid-rows-6 flex-1 gap-4 w-full">
                            {/* Now traverse over Dataset */}
                            {dataset.map((productData, index) => (
                                <ProductCard
                                productData={productData}
                                key={index}
                                className="col-span-1 row-span-1 bg-gray-100 rounded-sm h-96"
                                />
                            ))}
                        </div>
                    </div>
                    
                </div>
            </div>
            <div className="bg-red-400 w-full h-10">Pagination</div>
        </div>

    )
}