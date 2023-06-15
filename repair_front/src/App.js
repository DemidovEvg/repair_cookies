import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';
import Repair from './components/repair';
import Home from './components/home';
import Status from './components/status';
import "bootstrap/dist/css/bootstrap.css";


function App() {
  return (
    <div className="sub_body">
      <div className="top">


        <BrowserRouter>
          <Header />
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='repair' element={<Repair />} />
            <Route path='status' element={<Status />} />

          </Routes>
        </BrowserRouter>
        <Footer />
      </div>
    </div>
  );
}

export default App
