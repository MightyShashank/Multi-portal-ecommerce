import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home_page from './pages/Home_Page'
import Ontology_Page from './pages/Ontology_Page'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Product_Page from './pages/Product_Page'
import { DatasetProvider } from './DatasetContext';

function App() {
  return (
    <DatasetProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Home_page />} />
          <Route path="/add_ontology" element={<Ontology_Page />} />
          <Route path="/home_page" element={<Home_page />} />
          <Route path="/product_page" element={<Product_Page />} />
        </Routes>
      </Router>
    </DatasetProvider>
  );
}
export default App
