import {Navigate, useNavigate} from "react-router-dom";

function Repair({isAuth, makeOrder, notify}) {
  const navigate = useNavigate();
  let data = {
    'customerDescription': '',
    'category': ''
  }
  const handleChange = (event) => {
    console.log(event.target.value)
    data[[event.target.name]] = event.target.value
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!data["category"]) {
      notify("Выберите категорию техники");
      return;
    }
    makeOrder(data["category"], data["customerDescription"]);
    navigate("../account");
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
                    handleChange(event)
                  }}>
                    <option value="" className="grey-letters">Выберите категорию техники</option>
                    <option value="TELEPHONE">Мобильный телефон</option>
                    <option value="TABLET">Планшет</option>
                    <option value="LAPTOP">Ноутбук</option>
                  </select>
                  <textarea className="what-to-fix" name="customerDescription"
                            rows="6" placeholder="Описание неисправности"
                            onChange={event => {
                              handleChange(event)
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
