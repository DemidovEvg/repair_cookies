import React, {useState} from 'react';
import PhoneInput from 'react-phone-number-input/input';
import 'react-phone-number-input/style.css';
import {Navigate} from "react-router-dom";


function RegisterForm({isAuth, createClient, getToken, notify}) {
  const [password, setPassword] = useState('')
  const [password2, setPassword2] = useState('')
  const [phoneNumber, setPhoneNumber] = useState('')
  const [firstName, setFirstName] = useState('')
  const [patronymic, setPatronymic] = useState('')
  const [lastName, setLastName] = useState('')
  const [email, setEmail] = useState('')

  const handleSubmit = (event) => {
    event.preventDefault();
    const regexp = "[^A-Za-z][А-Яа-яЁё]{2,20}-?[А-Яа-яЁё]{0,20}[$А-Яа-яЁё]{1}$";

    if (password2 !== password) {
      notify('Пароли не совпадают');
      return;
    }

    if (!email) {
      notify('Поле email не может быть пустым');
      return;
    }

    if (!phoneNumber) {
      notify('Обязательно оставьте ваш номер телефона или нам придется спамить прямо на почту');
      return;
    }

    if (!firstName) {
      notify('Имя: обязательно для заполнения');
      return;
    }

    for (const name of [firstName, lastName, patronymic]) {
      const match = name.match(regexp)
      if (!match && !!name) {
        notify('Укажите ваше ФИО как в паспорте');
        return;
      }
    }

    const client = {
      'email': email,
      'password': password,
      'phoneNumber': phoneNumber,
      'firstName': firstName,
      'lastName': lastName,
      'patronymic': patronymic
    }

    createClient('api/users/', client);
  }

  return (
      <div className="site-content-wrap">
        <div className="nav-background"></div>
        <div className="site-content">
          <div className="form-holder">
            <div id="signup-form">
              <h1>РЕГИСТРАЦИЯ</h1>
              <fieldset>
                <form onSubmit={(event) => handleSubmit(event)}>
                  <input className="upper-field" name="lastName" type="text" placeholder="Фамилия"
                         onChange={({target}) => setLastName(target.value)}
                         title="Используйте кириллические символы"/>
                  <input className="middle-field" name="firstName" type="text" placeholder="Имя*"
                         onChange={({target}) => setFirstName(target.value)}
                         title="Используйте кириллические символы"/>
                  <input className="middle-field" name="patronymic" type="text" placeholder="Отчество"
                         onChange={({target}) => setPatronymic(target.value)}
                         title="Используйте кириллические символы"/>
                  <input className="middle-field"
                         onChange={({target}) => setEmail(target.value)}
                         name="email" type="text" placeholder="email*"/>
                  <PhoneInput
                      className="lower-field"
                      type="tel"
                      placeholder="номер телефона*"
                      defaultCountry="RU"
                      value={phoneNumber}
                      name="phoneNumber"
                      onChange={setPhoneNumber}
                  />
                  <p></p>
                  <input className="upper-field" type="password" placeholder="пароль*"
                         name="password"
                         onChange={({target}) => setPassword(target.value)}/>
                  <input className="lower-field" type="password" placeholder="повторите пароль"
                         name="password2"
                         onChange={({target}) => setPassword2(target.value)}/>
                  <input type="submit" value="ОТПРАВИТЬ"/>
                </form>
              </fieldset>
              {isAuth()
                  ? <Navigate to="/account"/>
                  : null}
            </div>
          </div>
        </div>
      </div>
  );
}

export default RegisterForm;