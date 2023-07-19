import {Form, Button} from "react-bootstrap";
import {Navigate, useNavigate} from "react-router-dom";

function Repair({isAuth, makeOrder}) {
  const navigate = useNavigate();
  let data = {
      'customerDescription': '',
      'category': 'TELEPHONE'
  }
  const handleChange = (event) => {
    data[[event.target.name]] = event.target.value
  };

  const handleSubmit = (event) => {
    event.preventDefault()
    makeOrder(data["category"], data["customerDescription"]);
    navigate("../account");
  }

  return (
      <div className="site-content-wrap">
        <div className="nav-background"></div>
        <div className="site-content">
          <h3 className="text-center">
            Оставить заявку на ремонт
          </h3>
          {isAuth()
              ? null
              : <Navigate to="/auth"/>}
          <div className="d-flex justify-content-center">
            <Form onSubmit={event => {
              handleSubmit()
            }}>

              <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Выберите категорию техники </Form.Label>
                <select name="category" onChange={event => {
                  handleChange(event)
                }}>
                  <option value="TELEPHONE">Мобильный телефон</option>
                  <option value="TABLET">Планшет</option>
                  <option value="LAPTOP">Ноутбук</option>
                </select>
              </Form.Group>

              <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Введите описание неисправности</Form.Label>
                <Form.Control type="textarea" name="customerDescription" placeholder="Разбитый экран" onChange={event => {
                  handleChange(event)
                }}/>
              </Form.Group>

              <Button variant="primary" type="submit" onClick={event => {
                handleSubmit(event)
              }}>
                Хочу ремонт
              </Button>
            </Form>
          </div>
        </div>
      </div>
  );
}

export default Repair;
