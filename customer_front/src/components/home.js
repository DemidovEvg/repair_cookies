import Carousel from 'react-bootstrap/Carousel';

function Home() {
  return (
    <div className="container-xxl">
      <Carousel>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src="https://wirelesstechcanada.ca/wp-content/uploads/2021/02/slide-11.jpg"
            alt="First slide"
          />
          <Carousel.Caption>
            <h3>Кто мы такие?</h3>
            <p>Мы высоко квалифицированные специалисты по доставке и ремонту смартфонов всех мастей</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src="https://assets-global.website-files.com/62460a17401634468363604e/631f1b3e59ed43fcec94ec69_tips-for-a-successful-mobile-phone-repair-in-vancouver.jpg"
            alt="Second slide"
          />

          <Carousel.Caption>
            <h3>Чего мы хотим?</h3>
            <p>Чтобы в мире не осталось ни одного испорченного телефона.</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src="https://img1.goodfon.com/original/1920x1080/e/65/electrical-circuits-puppets.jpg"
            alt="Third slide"
          />

          <Carousel.Caption>
            <h3>Что нам за это будет?</h3>
            <p>
              Хорший вопрос...
            </p>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    </div>


  );
}

export default Home;