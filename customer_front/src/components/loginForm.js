import {Component} from 'react';
import {NavLink, Navigate} from 'react-router-dom';


class LoginForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      "email": "",
      "password": ""
    }
  }

  handleChange(target) {
    this.setState({[target.name]: target.value});
  }

  handleSubmit(event) {
    event.preventDefault()
    this.props.getToken(this.state.email, this.state.password)
  }

  render() {
    return (
        <div className="site-content-wrap">
          <div className="nav-background"></div>
          <div className="site-content">
            <div className="form-holder">
              <div id="login-form">
                <h1>АВТОРИЗАЦИЯ</h1>
                <fieldset>
                  <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type="text" name='email' placeholder="email"
                           onChange={({target}) => this.handleChange(target)}/>
                    <input type="password" name='password' placeholder="пароль"
                           onChange={({target}) => this.handleChange(target)}/>
                    <input type="submit" value="ВОЙТИ"/>
                  </form>
                  <p>Впервые у нас? <NavLink to="../register">Зарегистрируйтесь</NavLink></p>
                </fieldset>
                {this.props.isAuth()
                    ? < Navigate to="../account"/>
                    : null}
              </div>
            </div>
          </div>
        </div>
    );
  }
}

export default LoginForm;