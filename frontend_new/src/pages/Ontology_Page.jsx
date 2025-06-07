import { useState } from "react";
import { Icon } from "@iconify/react"; 
import { useNavigate } from "react-router-dom";

export default function Ontology_Page({isOntologyOpen,setIsOntologyOpen}) {
  const Options = [
    { name: "Dashboard", description: "View all Ontology", icon: "akar-icons:dashboard" },
    { name: "API Ontology", description: "To create an Ontology", icon: "iconoir:database" },
    { name: "API Mappings", description: "To map to universal Ontology", icon: "mingcute:mind-map-line" },
  ];


  const [option, setOption] = useState("Dashboard");

  return (
    <div className="m-10 fixed inset-0 bg-black/100 bg-opacity-50 flex justify-start z-50">
      {/* Sidebar Panel */}
      <div className="w-96 bg-white h-full p-6 relative flex flex-col">
        
        {/* Close Button */}
        <button
          className="absolute top-4 right-4 text-gray-500 hover:text-black"
          onClick={() => setIsOntologyOpen(false)} 
        >
          <Icon icon="material-symbols:close" width="32" height="32" />
        </button>

        {/* Panel Content */}
        <h1 className="text-2xl font-bold text-sky-900 mb-8">Ontology Panel</h1>

        <div className="flex flex-col gap-y-4">
          {Options.map((item) => (
            <button
              key={item.name}
              onClick={() => setOption(item.name)}
              className={`flex items-center gap-3 px-4 py-2 rounded-md transition ${
                option === item.name ? "bg-sky-200 text-sky-900" : "hover:bg-gray-100"
              }`}
            >
              <Icon icon={item.icon} width="32" height="32" />
              <span className="text-lg">{item.name}</span>
            </button>
          ))}
        </div>

        {/* Selected Option Content */}
        <div className="mt-10 flex-1">
          <h2 className="text-xl font-bold text-sky-900">{option}</h2>
          {/* More content can go here */}
        </div>

      </div>
    </div>
  );
}



