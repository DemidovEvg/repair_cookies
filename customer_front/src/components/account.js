import {Navigate} from "react-router-dom";
function Order({order}) {
  if (!order) return
  return (
      <ul>
        <li>{`Заказ номер ${order.id}`}</li>
        <li>{`Заявленная неисправность: ${order.customerDescription}`}</li>
        <li>{`Замечания мастера: ${order.servicemanDescription}`}</li>
        <li>{`Статус ремонта: ${order.status}`}</li>
      </ul>
  );
}

function Orders({orders}) {
  return (
      <ol>
        {orders.map(order => {
          return (
              <li>
                <Order key={order.id} order={order}/>
                <hr/>
              </li>
          );
        })}
      </ol>
  );
}

function Account({orders, isAuth, logOut}) {
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
          <h3>
            Список заказов
          </h3>
          <hr/>
          <Orders orders={orders}/>
        </div>
      </div>
  );
}

export default Account;