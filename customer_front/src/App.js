import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';
import NotFound404 from './components/notfound';
import RegisterForm from './components/registerForm';
import LoginForm from './components/loginForm';
import Repair from './components/repair';
import Home from './components/home';
import Account from "./components/account";
import Contacts from "./components/contacts";
import Phones from "./components/phones";
import Prices from "./components/priceList";
import Cookies from 'universal-cookie';
import {ToastContainer, toast} from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';
import Notebooks from "./components/notebooks";
import Tablets from "./components/tablets";

function App() {
  const apiPath = process.env.REACT_APP_API_BACK;
  const url = new URL(apiPath)
  const [token, setToken] = useState('')
  const [email, setEmail] = useState('')
  const [users, setUsers] = useState([])
  const [orders, setOrders] = useState([])
  const [prices, setPrices] = useState([])

  const notify = (message) => {
    toast(`${message}`);
  }

  const createClient = (url, data) => {
    const headers = getHeaders();
    axios.post(apiPath + url, data, {'headers': headers}).then(response => {
      notify('Вы успешно зарегистрированы!');
      getToken(data.email, data.password);
    }).catch(error => {
          console.error('Что вообще могло пойти так?', error);
          let fieldName = ''
          for (const key in error.response.data) {
            if (key === 'phoneNumber') {
              fieldName = 'Номер телефона '
            } else if (key === 'email ') {
              fieldName = 'Email'
            } else if (key === "username") {
              continue;
            }
            notify(`${fieldName}${error.response.data[key]}`)
          }
        }
    );
  }

  const getToken = (email, password) => {
    const data = {
      'username': email,
      'password': password
    };
    axios.post(
        apiPath + 'api-token-auth/',
        data
    ).then(response => {
      saveToken(response.data['token'], email)
    })
        .catch(error => {
          console.error(error)
          notify('Похоже в email или пароль закралась ошибка.');
        });
  }


  const saveToken = (token, email = '') => {
    const cookie = new Cookies();
    cookie.set('token', token);
    cookie.set('email', email);
    cookie.set('SameSite', 'Lax');
    setToken(token);
    setEmail(email);
  }

  const restoreToken = () => {
    const cookie = new Cookies();
    const token = cookie.get('token');
    const email = cookie.get('email');
    setToken(token);
    setEmail(email);
  }

  const isAuth = () => {
    return !!token;
  }

  const getHeaders = () => {
    let headers = {
      "Content-Type": "application/json"
    };
    if (isAuth()) {
      headers['Authorization'] = 'Token ' + token
    }
    return headers;
  }


  const pullData = () => {
    if (!isAuth()) return;
    const headers = getHeaders()
    axios.get(
        apiPath + `api/users?email=${email}`,
        {'headers': headers}
    ).then(response => setUsers(response.data))
        .catch(error => console.error(`Что могло пойти так при обращении к users?`, error));

    axios.get(
        apiPath + `api/orders?email=${email}`,
        {'headers': headers}
    ).then(response => setOrders(response.data))
        .catch(error => console.error(`Что могло пойти так при обращении к orders?`, error));
  }


  const makeOrder = (category, customerDescription) => {
    const headers = getHeaders();
    const user = users[0]
    const data = {
      "client": {
        "id": user.id,
        "phoneNumber": user.phoneNumber
      },
      "category": category,
      "customerDescription": customerDescription
    }
    axios.post(
        apiPath + `api/orders/`,
        data,
        {'headers': headers}
    ).then(response => {
      notify("Ваша заявка на ремонт отправлена 🙌");
      pullData()
    })
        .catch(error => {
          console.error(error);
          notify('С вашего лицевого счета будет списано 5700 рублей, не забудьте пополнить баланс.');
        });
  }

  useEffect(() => {
    const headers = getHeaders()
    axios.get(
        apiPath + `api/prices`,
        {'headers': headers}
    ).then(response => setPrices(response.data))
        .catch(error => console.error(`Что могло пойти так при обращении к prices?`, error));
    restoreToken();
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    pullData();
    if (!!token) {
      const path = `ws://${url.host}/ws/client-orders/${email}/`
      const socket = new WebSocket(path)

      socket.onmessage = ((event) => {
        const data = JSON.parse(event.data);
        setOrders(data)
      })
    }
  }, [token]); // eslint-disable-line react-hooks/exhaustive-deps

  return (
      <div className="container sub-body">
        <BrowserRouter>
          <div className="sub-top">

            <Header
                isAuth={() => isAuth()}
                saveToken={() => {
                  saveToken('')
                }}
                logOut={() => {
                  saveToken('')
                }}
                users={users}
            />
            <ToastContainer/>
            <Routes>
              <Route path='/' element={<Home/>}/>
              <Route path='repair' element={<Repair
                  isAuth={() => isAuth()}
                  notify={(message) => notify(message)}
                  makeOrder={(category, customerDescription) => makeOrder(category, customerDescription)}/>}/>
              <Route path='contacts' element={<Contacts/>}/>
              <Route path='services' element={<Navigate to="/services/phones"/>}/>
              <Route path='/services/phones' element={<Phones prices={prices}/>}/>
              <Route path='/services/notebooks' element={<Notebooks prices={prices}/>}/>
              <Route path='/services/tablets' element={<Tablets prices={prices}/>}/>
              <Route path='prices' element={<Prices prices={prices}/>}/>
              <Route path='auth' element={<LoginForm
                  isAuth={() => isAuth()}
                  getToken={(email, password) => getToken(email, password)}/>}/>
              <Route path='account' element={<Account
                  orders={orders}
                  isAuth={() => isAuth()}
                  logOut={() => {
                    saveToken('')
                  }}
                  user={users}
                  email={email}
              />}/>
              <Route path='register' element={<RegisterForm
                  isAuth={() => isAuth()}
                  createClient={(url, data) => createClient(url, data)}
                  getToken={(email, password) => getToken(email, password)}
                  notify={(message) => notify(message)}/>}/>
              <Route path='*' element={<NotFound404/>}/>
            </Routes>
          </div>
          <Footer/>
        </BrowserRouter>
      </div>
  );
}

export default App
