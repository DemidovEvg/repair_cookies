import {Navigate, NavLink} from "react-router-dom";
import avatar from '../img/account-icon.svg'

function Order({order}) {
  if (!order) return
  return (
      <div>
        <p className="order-number"># {order.id.slice(24)}</p>
        <div className="order-details">
          <p className="order-date">{order.created.slice(0, 10)}</p>
          <p className="device-name">{order.model}</p>
          <p className="order-description">{order.servicemanDescription
              ? order.servicemanDescription
              : 'Отправлено на диагностику'}</p>
          <p className="order-status">{order.status}</p>
          <p className="order-price">{order.price
              ? order.price
              : (Math.random() * 1000).toFixed(2)}</p>
        </div>
      </div>
  );
}

function Orders({orders}) {
  return (
      <div>
        {orders.map(order => {
          return (
              <div key={order.id} className="order order-open">
                <Order order={order}/>
              </div>
          );
        })}
      </div>
  );
}

function Account({orders, isAuth, logOut, user}) {
  if (!user) {
    return
      }
  return (
      <div className="site-content-wrap">
        {isAuth()
            ? null
            : <Navigate to="/auth"/>}
        <div className="nav-background"></div>
        <div className="site-content">
          <div className="account-page-holder">
            <div className="user-name-and-user-phone">
              <div className="user-icon">
                <img src={avatar} alt="icon"/>
              </div>
              <div className="user-info">
                <p className="user-info-name">{user.lastName} {user.firstName} {user.patronymic}</p>
                <p className="user-mail">{user.email}</p>
                <p className="user-phone">{user.phoneNumber}</p>
                <div className="links-edit-or-call">
                  <NavLink className="account-link" to="../repair">Создать заказ</NavLink>
                  <NavLink className="account-link" to="../"
                           onClick={() => logOut()}
                  >Выйти</NavLink>
                </div>
              </div>
            </div>
            <div className="order-history">
              <div className="order-history-heading">История обслуживания</div>
              <Orders orders={orders}/>
            </div>
          </div>
        </div>
      </div>
  );
}

export default Account;