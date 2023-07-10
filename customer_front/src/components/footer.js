import logo from '../img/logo.svg';
import arrow from '../img/arrow.svg';
import hourglass from '../img/hourglass.svg';
import mailto from '../img/mailto.svg';
import destination from '../img/destination.svg';
import {Link} from "react-router-dom";


function Footer() {
  return (
      <footer>
        <div className="footer-top-wrap">
          <div className="footer-top">

            <div className="company-info footer-chld">
              <div className="footer-logo">
                <img src={logo} alt="logo-small"/>
              </div>
              <div className="owner-info">
                <div className="owner-doc">
                  <p className="text-to-style">ИП Иванов И.И.<br/>ИНН/ОГРНИП:<br/>
                    111111111111/22222222222222</p>
                </div>
                <p className="footer-disclaimer text-to-style lower">Обращаем ваше внимание на то, что
                  данный интернет-сайт носит исключительно информационный характер и ни
                  при каких условиях не является публичной офертой, определяемой положениями Статьи 437
                  (2) Гражданского
                  кодекса Российской Федерации.</p>
              </div>
            </div>

            <div className="link-info footer-chld">

              <ul className="link-list">
                <li className="link-item">
                  {/*<Link className="text-to-style" to="/" >ГЛАВНАЯ </Link>*/}
                </li>
                <li className="link-item">
                  <a className="text-to-style" href="#">О КОМПАНИИ</a>
                </li>
                <li className="link-item">

                  <a className="text-to-style" href="forum.html">ПРАЙС-ЛИСТ</a>
                </li>
                <li className="link-item">

                  <a className="text-to-style" href="blog-v1.html">ОТЗЫВЫ</a>
                </li>
                <li className="link-item">

                  <a className="text-to-style" href="#">КОНТАКТЫ</a>
                </li>
              </ul>

            </div>
            <div className="link-info footer-chld">

              <ul className="link-list">
                <li className="link-item">
                  <a className="text-to-style" href="#">УСЛУГИ</a>
                </li>
                <li className="link-item">
                  <a className="text-to-style" href="#">Ремонт&nbsp;компьютеров</a>
                </li>
                <li className="link-item">
                  <a className="text-to-style" href="#">Ремонт ноутбуков</a>
                </li>
                <li className="link-item">
                  <a className="text-to-style" href="#">Ремонт телефонов</a>
                </li>
                <li className="link-item">
                  <a className="text-to-style" href="#">Ремонт планшетов</a>
                </li>
              </ul>

            </div>
            <div className="contacts-info footer-chld">

              <ul className="foot-contacts-list">
                <li className="foot-contact-item foot-tel-num text-to-style">
                  <img src={arrow} alt=""/><p>+7 (969) 518-82-48</p>
                </li>
                <li className="foot-contact-item foot-tel-num text-to-style">
                  <img src={arrow} alt=""/><p>+7 (969) 518-82-48</p>
                </li>
                <li className="foot-contact-item text-to-style">
                  <img src={destination} alt=""/><p>г.Москва, ул. Строителей 42</p>
                </li>
                <li className="foot-contact-item text-to-style">
                  <img src={mailto} alt=""/><p>info@смартремонт.рф</p>
                </li>
                <li className="foot-contact-item text-to-style">
                  <img src={hourglass} alt=""/><p>10:00 - 20:00 (без выходных)</p>
                </li>
              </ul>

            </div>

          </div>
        </div>
        <div className="footer-bottom-wrap">
          <div className="footer-bottom">
            <hr/>
            <p><a className="text-to-style" href="http://СМАРТРЕМОНТ.РФ/">&copy;&nbsp;СМАРТ РЕМОНТ</a></p>
          </div>
        </div>
      </footer>
  );
}

export default Footer


