import { FiSearch } from 'react-icons/fi'; // Import magnifying glass icon from react-icons
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function SearchBar({
  placeholder = "Search for anything...",
  width = "w-64", // Default width (Tailwind class)
  height = "h-10", // Default height (Tailwind class)
  padding = "px-4", // Horizontal padding
  rounded = "rounded-sm", // Border radius
  iconSize = 18, // Icon size in pixels
  className = "", // Additional classes
  borderOptions = "",
  ...props // Other input props (onChange, value, etc.)
}) {

  const [query, setQuery] = useState('');
  const navigate = useNavigate();

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault(); // Prevent form submission or reload
      navigate('/product_page');
    }
  };

  return (
    <div className={`relative ${width} ${className}`}>
      <input type="text" 
      placeholder={placeholder} onKeyDown={handleKeyDown}
      className={`${width} ${height} ${padding} ${rounded} ${borderOptions} bg-white focus:outline-none pr-10`}
        {...props}
      />
      <FiSearch
        className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-800 pointer-events-none"
        size={iconSize}
      />
    </div>
  );
};