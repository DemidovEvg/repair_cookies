import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';
// import Repair from './components/repair';
// import Status from './components/status';
import "bootstrap/dist/css/bootstrap.css";


function App() {
  return (
    <div className="sub_body">
      <div className="top">

        <Header />
        <div>
          Услуги ремонта
        </div>
        <Footer />
      </div>
    </div>
  );
}

export default App
