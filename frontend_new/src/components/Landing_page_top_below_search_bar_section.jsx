import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../App.css'
import DeltaLogo from '../assets/DeltaLogo.svg'
import { Button } from "@/components/ui/button"
import { Icon } from "@iconify/react"
import SearchBar from '../components/ui/searchbar'
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectLabel,
    SelectTrigger,
    SelectValue,
  } from "@/components/ui/select"
import * as React from "react"
import { ChevronDown } from "lucide-react";
import {
    NavigationMenu,
    NavigationMenuContent,
    NavigationMenuIndicator,
    NavigationMenuItem,
    NavigationMenuLink,
    NavigationMenuList,
    NavigationMenuTrigger,
    NavigationMenuViewport,
  } from "@/components/ui/navigation-menu"
import { cn } from '@/lib/utils'
import Ontology_Page from '@/pages/Ontology_Page'
import { Link } from 'react-router-dom';

  const components = [
    {
      title: "Electronics",
      href: "/docs/primitives/alert-dialog",
      description:
        "A modal dialog that interrupts the user with important content and expects a response.",
    },
    {
      title: "Fashion",
      href: "/docs/primitives/hover-card",
      description:
        "For sighted users to preview content available behind a link.",
    },
    {
      title: "Computers and Accessories",
      href: "/docs/primitives/progress",
      description:
        "Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.",
    },
    {
      title: "Home Appliances",
      href: "/docs/primitives/scroll-area",
      description: "Visually or semantically separates content.",
    },
    {
      title: "Sports and Outdoors",
      href: "/docs/primitives/tabs",
      description:
        "A set of layered sections of content—known as tab panels—that are displayed one at a time.",
    },
    {
      title: "Toys and Games",
      href: "/docs/primitives/tooltip",
      description:
        "A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.",
    },
    {
      title: "Beauty and Personal Care",
      href: "/docs/primitives/tooltip",
      description:
        "A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.",
    },
    {
        title: "Books and Stationery",
        href: "/docs/primitives/tooltip",
        description:
          "A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.",
    },
  ]

export default function Landing_page_top_below_search_bar_section() {

    const [isOntologyOpen, setIsOntologyOpen] = useState(false);
    return (
        <div className="w-full h-16 pl-20 pr-25 flex justify-between items-center border-b-2 border-gray-400/30">
            
            {/* Menu */}
            

            {/* All category */}
            

            {/* Compare */}

            <NavigationMenu>
                <NavigationMenuList>

                    <NavigationMenuItem>
                        <NavigationMenuLink
                            href="/menu_side_bar"
                            className="pl-3 pr-3 py-2 text-sm font-medium hover:bg-gray-100 rounded-sm transition"
                        >
                            <div className="flex space-x-2 items-center">
                                <Icon icon="mynaui:sidebar" className='mt-0.5' style={{ width: "30px", height: "30px", color: "#555" }} />
                                <span className='text-base text-gray-600 items-center'>Menu</span>
                            </div>
                        </NavigationMenuLink>
                    </NavigationMenuItem>

                    {/* All Category */}
                    <NavigationMenuItem >
                        <NavigationMenuTrigger className="text-base rounded-sm [&>svg]:w-4 [&>svg]:h-4" style={{color: "#555" }}>All Category</NavigationMenuTrigger>
                        <NavigationMenuContent>
                            <ul className="grid w-[400px] gap-3 p-3 md:w-[500px] md:grid-cols-3 lg:w-[600px]">
                            {components.map((component) => (
                                <ListItem key={component.title} title={component.title} href={component.href}>
                                {component.description}
                                </ListItem>
                            ))}
                            </ul>
                        </NavigationMenuContent>
                    </NavigationMenuItem>

                    <NavigationMenuItem>
                        <NavigationMenuLink
                            href="/compare_ecommerce"
                            className="pl-3 pr-3 py-2 text-sm font-medium hover:bg-gray-100 rounded-sm transition"
                        >
                            <div className="flex space-x-2 items-center">
                            <Icon
                                icon="hugeicons:recycle-03"
                                className="transition-transform duration-300 hover:rotate-180"
                                style={{ width: "28px", height: "28px", color: "#555" }}
                            />
                                <span className='text-base text-gray-600 items-center'>Compare</span>
                            </div>
                        </NavigationMenuLink>
                    </NavigationMenuItem>

                    <>
                      <NavigationMenuItem>
                        <NavigationMenuLink asChild>
                          <Link
                            to="/add_ontology"
                            className="px-3 py-2 text-sm font-medium hover:bg-gray-100 rounded-sm transition"
                            onClick={(e) => {
                              e.preventDefault(); // Prevents the route change
                              setIsOntologyOpen(true);
                            }}
                          >
                            <div className="flex space-x-2 items-center">
                              <Icon
                                icon="mdi:graph-outline"
                                style={{ width: '28px', height: '28px', color: '#555' }}
                                className="transition-transform duration-300 hover:rotate-180"
                              />
                              <span className="text-base text-gray-600 items-center">Add Ontology</span>
                            </div>
                          </Link>
                        </NavigationMenuLink>
                      </NavigationMenuItem>

                      {/* Render modal outside the link */}
                      {isOntologyOpen && (
                        <div className="fixed inset-0 bg-black/50 z-50">
                          <Ontology_Page
                            isOntologyOpen={isOntologyOpen}
                            setIsOntologyOpen={setIsOntologyOpen}
                          />
                        </div>
                      )}

                  </>


                    <NavigationMenuItem>
                        <NavigationMenuLink
                            href="/settings"
                            className="px-3 py-2 text-sm font-medium hover:bg-gray-100 rounded-sm transition"
                        >
                            <div className="flex space-x-2 items-center">
                                <Icon icon="clarity:settings-line"  style={{ width: "28px", height: "28px", color: "#555" }}
                                className="transition-transform duration-300 hover:rotate-180 mt-0.5"
                            />
                                <span className='text-base text-gray-600 items-center'>Settings</span>
                            </div>
                        </NavigationMenuLink>
                    </NavigationMenuItem>

                </NavigationMenuList>
            </NavigationMenu>

        </div>
    )
}

const ListItem = React.forwardRef(({
    className,
    title,
    children,
    ...props
  }, ref) => {
    return (
      <li>
        <NavigationMenuLink asChild>
          <a
            ref={ref}
            className={cn(
              "block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground",
              className
            )}
            {...props}
          >
            <div className="text-sm font-medium leading-none">{title}</div>
            <p className="line-clamp-2 text-sm leading-snug text-muted-foreground">
              {children}
            </p>
          </a>
        </NavigationMenuLink>
      </li>
    )
  })
  
  ListItem.displayName = "ListItem"