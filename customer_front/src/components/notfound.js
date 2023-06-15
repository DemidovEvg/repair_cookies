import Modal from 'react-bootstrap/Modal';
import { useLocation } from 'react-router-dom';

function NotFound404() {
  const location = useLocation()
  return (
    <div className="container-xxl">
      <div className="d-flex justify-content-center">
        <Modal.Dialog>
          <Modal.Header>
            <Modal.Title>Ошибка 404</Modal.Title>
          </Modal.Header>

          <Modal.Body>
            <p>Страница по адресу"{location.pathname}" не найдена</p>
          </Modal.Body>
        </Modal.Dialog>
      </div>
    </div>
  );
}

export default NotFound404
