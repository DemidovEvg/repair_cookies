import { Form, Button } from "react-bootstrap";

function Status({ checkStatus }) {
  let orderNumber = '';
  const handleChange = (event) => {
    orderNumber = event.target.value
  };

  const handleSubmit = () => {
    checkStatus(orderNumber);
  };

  return (
    <div className="container-xxl">
      <h3 className="text-center">
        Проверка состояния ремонта
      </h3>
      <div className="d-flex justify-content-center">
        <Form onSubmit={() => { handleSubmit() }}>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Введите номер Вашего заказа</Form.Label>
            <Form.Control type="text" placeholder="ХХХХХХХХ" onChange={(event) => { handleChange(event) }} />
          </Form.Group>
          <Button variant="primary" type="submit">
            Узнать статус
          </Button>
        </Form>
      </div>
    </div>

  );
}

export default Status;