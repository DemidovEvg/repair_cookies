import React, { Component } from 'react';
import Form from 'react-bootstrap/Form';
import { Link } from 'react-router-dom';


class LoginForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      "username": "",
      "password": ""
    }
  }

  handleChange(target) {
    this.setState({ [target.name]: target.value });
  }

  handleSubmit(event) {
    alert(`Пользователь ${this.state.username} авторизован`);
  }

  render() {
    return (
      <div className="container-xxl">
        <div className="d-flex justify-content-center">
          <Form onSubmit={(event) => this.handleSubmit(event)}>
            <Form.Group className="mb-3" controlId="formBasicText">
              <Form.Label>Username</Form.Label>
              <Form.Control type="text" name="username" placeholder="Username"
                onChange={({ target }) => this.handleChange(target)} />
              <Form.Text className="text-muted">
                Ввеите имя пользователя.
              </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" name="password" placeholder="Password"
                onChange={({ target }) => this.handleChange(target)} />
              <Form.Text className="text-muted">
                Ввеите пароль.
              </Form.Text>
            </Form.Group>

            <Link className='btn btn-primary' to='../'
              onClick={(event) => this.handleSubmit(event)}>Submit</Link>
          </Form>
        </div>
      </div>
    );
  }
}

export default LoginForm;