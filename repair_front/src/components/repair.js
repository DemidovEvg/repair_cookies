import { Form, Button } from "react-bootstrap";

function Repair() {
  return (
    <div className="container-xxl">
      <h3>
        Оставить заявку на ремонт
      </h3>
      <div className="d-flex justify-content-center">
        <Form>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Введите Ваш номер телефона</Form.Label>
            <Form.Control type="text" placeholder="+7-ХХХ-ХХХ-ХХ-ХХ" />
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

  );
}

export default Repair;
