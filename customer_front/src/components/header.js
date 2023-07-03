import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

function Header({ isAuth, logOut }) {
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="/">Смарт Ремонт</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/repair">Услуги ремонта</Nav.Link>
            <Nav.Link href="/status">Проверка статуса</Nav.Link>
            {isAuth()
              ? <Nav.Link className='nav-link' to="/" onClick={() => logOut()}>Выйти</Nav.Link>
              : <Nav.Link href="/auth">Войти</Nav.Link>}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Header;