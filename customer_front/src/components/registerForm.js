import React, {Component} from 'react';
import Form from 'react-bootstrap/Form';
import PhoneInput from 'react-phone-number-input';
import 'react-phone-number-input/style.css';
import {Button} from "react-bootstrap";
import {Navigate} from "react-router-dom";


class RegisterForm extends Component {
  constructor(props) {
    super(props)
    this.state = {
      'password': '',
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
    event.preventDefault()
    this.props.createClient('api/users/', this.state);
  }

  render() {
    return (
        <div className="site-content-wrap">
          <div className="nav-background"></div>
          <div className="site-content">
            <div className="d-flex justify-content-center">
              <Form>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Label>Email</Form.Label>
                  <Form.Control type="email" name="email" placeholder="user@domain.com"
                                onChange={({target}) => this.handleChange(target)}/>
                </Form.Group>
                <Form.Group className="mb-3" controlId="formBasicPhone">
                  <Form.Label>Номер вашего телефона</Form.Label>
                  <PhoneInput
                      placeholder="+7ХХХХХХХХХХ"
                      defaultCountry="RU"
                      value={this.state.phoneNumber}
                      name="phoneNumber"
                      onChange={phoneNumber => this.setState({phoneNumber})}
                  />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Пароль</Form.Label>
                  <Form.Control type="password" name="password" placeholder="Password"
                                onChange={({target}) => this.handleChange(target)}/>
                </Form.Group>

                <Form.Group className="mb-3" controlId="formLastName">
                  <Form.Label>Фамилия</Form.Label>
                  <Form.Control type="text" name="lastName" placeholder="Иванов"
                                onChange={({target}) => this.handleChange(target)}/>
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicFirstName">
                  <Form.Label>Имя</Form.Label>
                  <Form.Control type="text" name="firstName" placeholder="Иван"
                                onChange={({target}) => this.handleChange(target)}/>
                </Form.Group>

                <Form.Group className="mb-3" controlId="formPatronymic">
                  <Form.Label>Отчество</Form.Label>
                  <Form.Control type="text" name="patronymic" placeholder="Иванович"
                                onChange={({target}) => this.handleChange(target)}/>
                </Form.Group>
                <Button variant="primary" type="submit" onClick={(event) => this.handleSubmit(event)}>
                  Регистрация
                </Button>

              </Form>
              {this.props.isAuth()
                  ? <Navigate to="../account"/>
                  : null}
            </div>
          </div>
        </div>
    );
  }
}

export default RegisterForm;