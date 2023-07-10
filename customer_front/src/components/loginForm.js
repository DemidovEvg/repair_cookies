import {Button} from 'react-bootstrap';
import React, {Component} from 'react';
import Form from 'react-bootstrap/Form';
import {Navigate} from 'react-router-dom';


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
                <Form.Label>Username</Form.Label>
                <Form.Control type="text" name="username" placeholder="Username"
                              onChange={({target}) => this.handleChange(target)}/>
                <Form.Text className="text-muted">
                  Введите имя пользователя.
                </Form.Text>
              </Form.Group>

              <Form.Group className="mb-3" controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" name="password" placeholder="Password"
                              onChange={({target}) => this.handleChange(target)}/>
                <Form.Text className="text-muted">
                  Введите пароль.
                </Form.Text>
              </Form.Group>

              {/* <Link className='btn btn-primary' to='../'
              onClick={(event) => this.handleSubmit(event)}>Submit</Link> */}
              <Button variant="primary" type="submit">
                Submit
              </Button>
            </Form>
            {this.props.isAuth()
                ? < Navigate to="/"/>
                : null}
          </div>
        </div>
    );
  }
}

export default LoginForm;