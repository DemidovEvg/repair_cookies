import React, { Component } from 'react';
import axios from 'axios';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';
import NotFound404 from './components/notfound';
import RegisterForm from './components/registerForm';
import LoginForm from './components/loginForm';
import Repair from './components/repair';
import Home from './components/home';
import Status from './components/status';
import "bootstrap/dist/css/bootstrap.css";

class App extends Component {
  constructor(props) {
    super(props)
    this.apiPath = 'https://delivery.error';
    this.state = {
      'token': '',
    }
  }


  makeOrder(clientNumber) {
    axios.post(this.apiPath, { "clientNumber": clientNumber })
      .then(response => {
        alert("Взяли и починили.")
      })
      .catch(error => alert('С вашего лицевого счета будет списано 5700 рублей, не забудьте пополнить баланс.'));
  }

  checkStatus(orderNumber) {
    axios.get(`${this.apiPath}/status?order=${orderNumber}`)
      .then(response => {
        alert("Можно забирать.")
      })
      .catch(error => alert('Еще не готово.'));
  }

  render() {
    return (
      <div className="sub_body">
        <div className="top">
          <BrowserRouter>
            <Header />
            <Routes>
              <Route path='/' element={<Home />} />
              <Route path='repair' element={<Repair makeOrder={(clientNumber) => this.makeOrder(clientNumber)} />} />
              <Route path='status' element={<Status checkStatus={(orderNumber) => this.checkStatus(orderNumber)} />} />
              <Route path='auth' element={<LoginForm/>} />
              <Route path='auth/register' element={<RegisterForm />} />
              <Route path='*' element={<NotFound404 />} />
            </Routes>
          </BrowserRouter>
        </div>
        <div className='footer'>
          <Footer />
        </div>
      </div>
    );
  }
}

export default App
