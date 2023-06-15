import { Form, Button } from "react-bootstrap";

function Status() {
  return (
    <div className="container-xxl">
      <h3>
        Проверка состояния ремонта
      </h3>
      <div className="d-flex justify-content-center">
        <Form>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Введите номер Вашего заказа</Form.Label>
            <Form.Control type="text" placeholder="ХХХХХХХХ" />
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