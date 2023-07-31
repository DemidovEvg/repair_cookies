import {Navigate, useNavigate} from "react-router-dom";
import {useState} from "react";

function Repair({isAuth, makeOrder, notify}) {
  const navigate = useNavigate();
  const [category, setCategory] = useState('')
  const [customerDescription, setCustomerDescription] = useState('')

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!category) {
     notify("Выберите категорию техники");
     return;
    }    makeOrder(category, customerDescription);
    navigate("/account");
  }

  return (
      <div className="site-content-wrap">
        {isAuth()
            ? null
            : <Navigate to="/auth"/>}
        <div className="nav-background"></div>
        <div className="site-content">
          <div className="form-holder">
            <div id="signup-form">
              <h1>ОСТАВИТЬ ЗАЯВКУ НА РЕМОНТ</h1>
              <fieldset>
                <form onSubmit={(event) => {
                  handleSubmit(event)
                }}>
                  <select className="device-type" name="category" onChange={event => {
                    setCategory(event.target.value)
                  }}>
                    <option value="" className="grey-letters">Выберите категорию техники</option>
                    <option value="TELEPHONE">Мобильный телефон</option>
                    <option value="TABLET">Планшет</option>
                    <option value="LAPTOP">Ноутбук</option>
                  </select>
                  <textarea className="what-to-fix" name="customerDescription"
                            rows="6" placeholder="Описание неисправности"
                            onChange={event => {
                              setCustomerDescription((event.target.value))
                            }}>
                </textarea>
                  <input type="submit" value="ОТПРАВИТЬ"/>
                </form>
              </fieldset>
            </div>
          </div>
        </div>
      </div>
  );
}

export default Repair;
