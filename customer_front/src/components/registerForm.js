import React, { Component } from 'react';
import Form from 'react-bootstrap/Form';
import { Link } from 'react-router-dom';
import PhoneInput from 'react-phone-number-input';
import 'react-phone-number-input/style.css';


class RegisterForm extends Component {
  constructor(props) {
    super(props)
    this.state = {
      'username': '',
      'password': '',
      'firstName': '',
      'phone': '',
      'lastName': '',
      'email': ''
    }
  }

  handleChange(target) {
    this.setState({ [target.name]: target.value });
  }

  handleSubmit() {
    alert(`Пользователь ${this.state.username} создан`);
  }

  render() {
    return (
      <div className="container-xxl">
        <div className="d-flex justify-content-center">
          <Form>
            <Form.Group className="mb-3" controlId="formBasicText">
              <Form.Label>Username</Form.Label>
              <Form.Control type="text" name="username" placeholder="Username"
                onChange={({ target }) => this.handleChange(target)} />
              <Form.Text className="text-muted">
                Enter your unique username here.
              </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPhone">
              <Form.Label>Phone Number</Form.Label>
              <PhoneInput
                placeholder="Enter phone number"
                defaultCountry="RU"
                value={this.state.phone}
                name="Phone"
                onChange={phone => this.setState({ phone })}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" name="password" placeholder="Password"
                onChange={({ target }) => this.handleChange(target)} />
              <Form.Text className="text-muted">
                Пароль на эльфийском.
              </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicFirstName">
              <Form.Label>First name</Form.Label>
              <Form.Control type="text" name="firstName" placeholder="First Name"
                onChange={({ target }) => this.handleChange(target)} />
              <Form.Text className="text-muted">
                Enter your first name here.
              </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formLastName">
              <Form.Label>Last name</Form.Label>
              <Form.Control type="text" name="lastName" placeholder="Last name"
                onChange={({ target }) => this.handleChange(target)} />
              <Form.Text className="text-muted">
                Enter your second name here.
              </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Email</Form.Label>
              <Form.Control type="email" name="email" placeholder="user@domain.com"
                onChange={({ target }) => this.handleChange(target)} />
              <Form.Text className="text-muted">
                Enter your electronic post address here.
              </Form.Text>
            </Form.Group>

            <Link className='btn btn-primary' to='#'
              onClick={(event) => this.handleSubmit(event)}>Submit</Link>
          </Form>
        </div>
      </div>
    );
  }
}

export default RegisterForm;