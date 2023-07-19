import arrow from '../img/arrow.svg';
import hourglass from '../img/hourglass.svg';
import mailto from '../img/mailto.svg';
import destination from '../img/destination.svg';
import {NavLink} from "react-router-dom";


function Footer() {
  return (
      <footer>
        <div className="footer-top-wrap">
          <div className="footer-top">

            <div className="company-info footer-chld">
              <div className="footer-logo">
                <img src={require('../img/logo.png')} alt="logo-small"/>
              </div>
              <div className="owner-info">
                <div className="owner-doc">
                  <p className="text-to-style">ИП Ибатуллин Р.Г.
                    <br/>
                    ИНН: 19844654754324
                    <br/>
                    ОГРНИП: 569239521340
                    <br/>
                  </p>
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
                  <NavLink className="text-to-style" to="../" >ГЛАВНАЯ </NavLink>
                </li>
                <li className="link-item">
                  <NavLink className="text-to-style" to="../prices">ПРАЙС-ЛИСТ</NavLink>
                </li>
                <li className="link-item">
                  <a className="text-to-style"
                     href="https://otzovik.com/reviews/oficialniy_servisniy_centr_smart-pro_russia_moscow/">ОТЗЫВЫ</a>
                </li>
                <li className="link-item">
                  <NavLink to="../contacts" className="text-to-style" >КОНТАКТЫ</NavLink>
                </li>
              </ul>

            </div>
            <div className="link-info footer-chld">

              <ul className="link-list">
                <li className="link-item">
                  <NavLink className="text-to-style" to="../prices">УСЛУГИ</NavLink>
                </li>
                <li className="link-item">
                  <NavLink className="text-to-style" to="../notebooks">Ремонт ноутбуков</NavLink>
                </li>
                <li className="link-item">
                  <NavLink className="text-to-style" to="../phones">Ремонт телефонов</NavLink>
                </li>
                <li className="link-item">
                  <NavLink className="text-to-style" to="../tablets">Ремонт планшетов</NavLink>
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
            <p className="text-to-style">&copy;&nbsp;СМАРТ РЕМОНТ</p>
          </div>
        </div>
      </footer>
  );
}

export default Footer


