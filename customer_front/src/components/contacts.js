import destination from '../img/destination.svg';
import hourglass from '../img/hourglass.svg';
import phone from '../img/con_phone.svg';
import mailto from '../img/mailto.svg';
import { YMaps, Panorama } from "@pbe/react-yandex-maps";


function Contacts() {
  return (
      <div className="site-content-wrap">
        <div className="nav-background"></div>
        <div className="site-content">
          <div className="contacts-header">
            <div className="container">
              <h2 className="contacts__header">КОНТАКТЫ</h2>
            </div>

          </div>
          <div className="map-and-contacts">
            <div className="map-container">
              <iframe
                  src="https://yandex.ru/map-widget/v1/?um=constructor%3A433590ee05406b466ca6632b72d01817145b7ca526c7a8841c6e58bb89d349f9&amp;source=constructor"
                  width="1080" height="600" ></iframe>
            </div>

            <div className="contacts-contacts">
              <ul className="contacts-list">
                <li className="contact-item ">
                  <img src={destination} alt=""/>
                  <p>г.Москва, ул. Строителей д.3</p>
                </li>
                <li className="contact-item ">
                  <img src={hourglass} alt=""/>
                  <p>10:00 - 20:00 (без выходных)</p>
                </li>
                <li className="contact-item-telephone-number">
                  <img src={phone} alt=""/>
                  <p>+ 7 (789) 456-12-34</p>
                </li>
                <li className="contact-item-telephone-number">
                  <img src={phone} alt=""/>
                  <p>+ 7 (789) 456-12-34</p>
                </li>
                <li className="contact-item">
                  <img src={mailto} alt=""/>
                  <p>info@смартремонт.рф</p>
                </li>

              </ul>

              <div className="contacts-owner-info">
                <p className="contacts-disclaimer">Если у вас возникли проблемы с ноутбуком, телефоном или
                  планшетом. Если вы заметили странности в ее работе, пожалуйста,
                  свяжитесь с нами. Вы можете позвонить нам по указанным номерам телефона или написать на
                  электронную почту. Мы гарантируем быстрое и качественное решение проблем с вашей
                  техникой.
                </p>
              </div>

            </div>
          </div>


        </div>
      </div>
  );
}

export default Contacts;