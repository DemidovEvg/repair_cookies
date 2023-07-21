import {useLocation} from 'react-router-dom';

function NotFound404() {
  const location = useLocation()
  return (
      <div className="site-content-wrap">
        <div className="nav-background"></div>
        <div className="site-content">

          <div className="picture-404">
            <div>
              <big>404</big>
              <p>Страница по адресу <big>{location.pathname}</big> не найдена</p>
            </div>
            <img src={require('../img/Man note 1.png')} alt="Страница по адресу не найдена"/>
          </div>
        </div>
      </div>
  );
}

export default NotFound404
