import { Navigate, NavLink } from "react-router-dom";
import avatar from '../img/account-icon.svg'

const googleTranslateApi = {
  "CREATED": "Заявка создана",
  "GETTING_FROM_CLIENT": "Получение техники от клиента",
  "SENT_TO_REPAIR": "Доставлен в службу ремонта",
  "REPAIR_IN_PROCESS": "Ремонт начат",
  "REPAIR_DONE": "Ремонт закончен",
  "SENDING_TO_CLIENT": "Доставка техники клиенту",
  "CLOSED": "Заявка закрыта"
}
function User({ user, logOut, email }) {
  if (!user) return
  return <div className="user-info">
    <p className="user-info-name">{user.lastName} {user.firstName} {user.patronymic}</p>
    <p className="user-mail">{email}</p>
    <p className="user-phone">{user.phoneNumber}</p>
    <div className="links-edit-or-call">
      <NavLink className="account-link" to="/repair">Создать заказ</NavLink>
      &nbsp;
      <NavLink className="account-link" to="/"
        onClick={() => logOut()}
      >Выйти</NavLink>
    </div>
  </div>
}

function Order({ order }) {
  if (!order) return
  console.log(order)
  return (
    <div>
      <p className="order-number"># {order.id.slice(24)}</p>
      <div className="order-details">
        <p className="order-date">{order.created.slice(0, 10)}</p>
        <p className="device-name">{order.model}</p>
        <p className="order-description">{order.servicemanDescription
          ? order.servicemanDescription
          : 'Отправлено на диагностику'}</p>
        <p className="order-status">{googleTranslateApi[order.status]}</p>
        <p className="order-price">{order.amountDueBy
          ? order.amountDueBy + ' руб.'
          : '-'}</p>
        <p className="order-payment-completed">{order.paymentCompleted
          ? "Оплата произведена"
          : ''}</p>
      </div>
    </div>
  );
}

function Empty() {
  return (
    <div className="order order-open">
      <p className="order-number"></p>
      <div className="order-details">
        &nbsp;&nbsp;Вы еще ничего не заказали ;)
      </div>
    </div>
  );
}

function Orders({ orders }) {
  return (
    <div>
      {orders.map(order => {
        return (
          <div key={order.id} className="order order-open">
            <Order order={order} />
          </div>
        );
      })}
    </div>
  );
}

function Account({ orders, isAuth, logOut, user, email }) {
  return (
    <div className="site-content-wrap">
      {isAuth()
        ? null
        : <Navigate to="/auth" />}
      <div className="nav-background"></div>
      <div className="site-content">
        <div className="account-page-holder">
          <div className="user-name-and-user-phone">
            <div className="user-icon">
              <img src={avatar} alt="icon" />
            </div>
            <User user={user[0]} logOut={logOut} email={email} />
          </div>
          <div className="order-history">
            <div className="order-history-heading">История обслуживания</div>
            {orders.length > 0
              ? <Orders orders={orders} />
              : <Empty />}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Account;