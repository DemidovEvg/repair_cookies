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
import Cookies from 'universal-cookie';

class App extends Component {
  constructor(props) {
    super(props)
    this.apiPath = 'http://localhost:8001/';
    this.state = {
      'token': '',
      'username': '',
    }
  }

  getToken(username, password) {
    const data = {
      'username': username,
      'password': password
    };
    axios.post(
      this.apiPath + 'api-token-auth/',
      data
    ).then(response => {
      this.saveToken(response.data['token'], username)
    })
      .catch(error => alert('Wrong value of username or password'));
  }


  saveToken(token, username = '') {
    const cookie = new Cookies();
    cookie.set('token', token);
    cookie.set('username', username);
    cookie.set('SameSite', 'Lax');
    this.setState({ 'token': token, 'username': username }, () => this.pullData());
  }

  restoreToken() {
    const cookie = new Cookies();
    const token = cookie.get('token');
    const username = cookie.get('username');
    this.setState({ 'token': token, 'username': username }, () => this.pullData());
  }

  isAuth() {
    return !!this.state.token;
  }

  getHeaders() {
    let headers = {
      "Content-Type": "application/json"
    };
    if (this.isAuth()) {
      headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers;
  }


  pullData() {
    const headers = this.getHeaders();

    axios.get(
      this.apiPath + 'api/orders/',
      { 'headers': headers }
    ).then(response => {
      console.log(response.data)
    }).catch(
      error => console.log('Что могло пойти так?'));
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

  componentDidMount() {
    this.restoreToken();
  }

  render() {
    return (
      <div className="sub_body">
        <div className="top">
          <BrowserRouter>
            <Header
              isAuth={() => this.isAuth()}
              saveToken={() => { this.saveToken('') }}
              logOut={() => { this.saveToken('') }} />
            <Routes>
              <Route path='/' element={<Home />} />
              <Route path='repair' element={<Repair
                makeOrder={(clientNumber) => this.makeOrder(clientNumber)} />} />
              <Route path='status' element={<Status
                checkStatus={(orderNumber) => this.checkStatus(orderNumber)} />} />
              <Route path='auth' element={<LoginForm
                isAuth={() => this.isAuth()}
                getToken={(username, password) => this.getToken(username, password)} />} />
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
