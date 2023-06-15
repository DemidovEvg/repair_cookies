import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

function Header() {
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="#home">Cookies Service</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#home">Услуги ремонта</Nav.Link>
            <Nav.Link href="#link">Провепка статуса</Nav.Link>
            <NavDropdown title="Крутые фичи" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Мощная фича</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">
                Супер фича
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Улётная фича</NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Header;