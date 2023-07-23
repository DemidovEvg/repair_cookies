import React, {Component} from 'react';
import PhoneInput from 'react-phone-number-input';
import 'react-phone-number-input/style.css';
import {Navigate} from "react-router-dom";


class RegisterForm extends Component {
  constructor(props) {
    super(props)
    this.state = {
      'password': '',
      'password2': '',
      'phoneNumber': '',
      'firstName': '',
      'patronymic': '',
      'lastName': '',
      'email': ''
    }
  }

  handleChange(target) {
    this.setState({[target.name]: target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    const regexp = "[^A-Za-z][А-Яа-яЁё]{2,20}-?[А-Яа-яЁё]{0,20}[$А-Яа-яЁё]{1}"
    if (this.state.password2 !== this.state.password) {
      this.props.notify('Пароли не совпадают');
      return;
    }
    if (!this.state.firstName) {
      this.props.notify('Имя: обязательно для заполнения');
      return;
    }
    for (const name of [this.state.firstName, this.state.lastName, this.state.patronymic]) {
      const match = name.match(regexp)
      if (!match && !!name) {
        this.props.notify('Укажите ваше ФИО как в паспорте');
        return;
      }
    }
    this.props.createClient('api/users/', this.state);
  }

  render() {
    return (
        <div className="site-content-wrap">
          <div className="nav-background"></div>
          <div className="site-content">
            <div className="form-holder">
              <div id="signup-form">
                <h1>РЕГИСТРАЦИЯ</h1>
                <fieldset>
                  <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input className="upper-field" name="lastName" type="text" placeholder="Фамилия"
                           onChange={({target}) => this.handleChange(target)}
                           title="Используйте кириллические символы"/>
                    <input className="middle-field" name="firstName" type="text" placeholder="Имя*"
                           onChange={({target}) => this.handleChange(target)}
                           title="Используйте кириллические символы"/>
                    <input className="middle-field" name="patronymic" type="text" placeholder="Отчество"
                           onChange={({target}) => this.handleChange(target)}
                           title="Используйте кириллические символы"/>
                    <input className="middle-field"
                           onChange={({target}) => this.handleChange(target)}
                           name="email" type="text" placeholder="email*"/>
                    <PhoneInput
                        className="lower-field"
                        type="tel"
                        placeholder="номер телефона*"
                        defaultCountry="RU"
                        value={this.state.phoneNumber}
                        name="phoneNumber"
                        onChange={phoneNumber => this.setState({phoneNumber})}
                    />
                    <p></p>
                    <input className="upper-field" type="password" placeholder="пароль"
                           name="password"
                           onChange={({target}) => this.handleChange(target)}/>
                    <input className="lower-field" type="password" placeholder="повторите пароль"
                           name="password2"
                           onChange={({target}) => this.handleChange(target)}/>
                    <input type="submit" value="ОТПРАВИТЬ"/>
                  </form>
                </fieldset>
                {this.props.isAuth()
                    ? <Navigate to="../account"/>
                    : null}
              </div>
            </div>
          </div>
        </div>
    );
  }
}

export default RegisterForm;