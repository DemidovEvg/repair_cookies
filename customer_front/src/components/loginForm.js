import {Button} from 'react-bootstrap';
import React, {Component} from 'react';
import Form from 'react-bootstrap/Form';
import {NavLink, Navigate} from 'react-router-dom';


class LoginForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      "username": "",
      "password": ""
    }
  }

  handleChange(target) {
    this.setState({[target.name]: target.value});
  }

  handleSubmit(event) {
    event.preventDefault()
    this.props.getToken(this.state.username, this.state.password)
  }

  render() {
    return (
        <div className="site-content-wrap">
          <div className="nav-background"></div>
          <div className="site-content">
            <Form onSubmit={(event) => this.handleSubmit(event)}>
              <Form.Group className="mb-3" controlId="formBasicText">
                <Form.Label>Email</Form.Label>
                <Form.Control type="email" name="username" placeholder="email@address.com"
                              onChange={({target}) => this.handleChange(target)}/>
              </Form.Group>

              <Form.Group className="mb-3" controlId="formBasicPassword">
                <Form.Label>Пароль</Form.Label>
                <Form.Control type="password" name="password" placeholder="Password"
                              onChange={({target}) => this.handleChange(target)}/>
              </Form.Group>

              <Button variant="primary" type="submit">
                Войти
              </Button>
            </Form>
            <NavLink to="../register">Регистрация</NavLink>

            {this.props.isAuth()
                ? < Navigate to="../account"/>
                : null}
          </div>
        </div>
    );
  }
}

export default LoginForm;