import {Form, Button} from "react-bootstrap";
import {Navigate} from "react-router-dom";

function Repair({isAuth, makeOrder}) {
  let clientNumber = '';
  const handleChange = (event) => {
    clientNumber = event.target.value
  };

  const handleSubmit = () => {
    makeOrder(clientNumber);
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
                <Form.Label>Введите Ваш номер телефона</Form.Label>
                <Form.Control type="text" placeholder="+7XXXXXXXXXX" onChange={event => {
                  handleChange(event)
                }}/>
                <Form.Text className="text-muted">
                  Мы не передаём информацию третьим лица, наверно.
                </Form.Text>
              </Form.Group>
              <Button variant="primary" type="submit">
                Хочу ремонт
              </Button>
            </Form>
          </div>
        </div>
      </div>
  );
}

export default Repair;
