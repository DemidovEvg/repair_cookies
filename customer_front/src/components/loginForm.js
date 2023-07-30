import {useState} from 'react';
import {NavLink, Navigate} from 'react-router-dom';


function LoginForm ({isAuth, getToken}) {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = (event) => {
    event.preventDefault();
    getToken(email, password);
  }

  return (
      <div className="site-content-wrap">
        <div className="nav-background"></div>
        <div className="site-content">
          <div className="form-holder">
            <div id="login-form">
              <h1>АВТОРИЗАЦИЯ</h1>
              <fieldset>
                <form onSubmit={(event) => handleSubmit(event)}>
                  <input type="text" name='email' placeholder="email"
                         onChange={({target}) => setEmail(target.value)}/>
                  <input type="password" name='password' placeholder="пароль"
                         onChange={({target}) => setPassword(target.value)}/>
                  <input type="submit" value="ВОЙТИ"/>
                </form>
                <p>Впервые у нас? <NavLink to="/register">Зарегистрируйтесь</NavLink></p>
              </fieldset>
              {isAuth()
                  ? < Navigate to="/account"/>
                  : null}
            </div>
          </div>
        </div>
      </div>
  );
}

export default LoginForm;