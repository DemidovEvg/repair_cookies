import {Navigate} from "react-router-dom";

function Account({isAuth, logOut}) {
  return (

      <div className="site-content-wrap">
        {isAuth()
            ? null
            : <Navigate to="/auth"/>}
        <div className="nav-background"></div>
        <div className="site-content">
          <h2>
            Личный кабинет
          </h2>

          <button onClick={() => logOut()}>Выйти</button>
        </div>
      </div>
  );
}

export default Account;