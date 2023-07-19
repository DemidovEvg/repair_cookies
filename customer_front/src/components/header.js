import arrow from '../img/arrow.svg';
import icon1 from '../img/sn-icon-1.svg'
import icon2 from '../img/sn-icon-2.svg'
import divider from '../img/divider.svg'
import {NavLink} from "react-router-dom";


function Header({isAuth, logOut}) {
  return (
      <header>
        <div className="site-nav">
          <div className="logo">
            <img src={require('../img/logo.png')} alt="logo"/>
          </div>
          <div className="phones-and-nav">
            <div className="phones">
              <img src={arrow} alt="->"/>
              <p className="tel-num">+ 7 (789) 456-12-34</p>
              <img src={arrow} alt="->"/>
              <p className="tel-num">+ 7 (789) 456-12-34</p>
              <img src={icon1} alt="WhatsApp_icon"/>
              <img src={icon2} alt="telegram_icon"/>
            </div>
            <div className="links">
              <ul className="linkslist">
                <li><NavLink className="link" to="../">&nbsp;ГЛАВНАЯ&nbsp;</NavLink></li>
                <li className="divider"><img src={divider} alt=""/></li>
                <li className="services"><NavLink to="../prices">&nbsp;УСЛУГИ&nbsp;</NavLink>
                  <ul className="dropdown">
                    <li><NavLink to="../phones">Ремонт телефонов</NavLink></li>
                    <li>
                      <hr/>
                    </li>
                    <li><NavLink to="../tablets">Ремонт планшетов</NavLink></li>
                    <li>
                      <hr/>
                    </li>
                    <li><NavLink to="../notebooks">Ремонт ноутбуков</NavLink></li>
                  </ul>
                </li>
                <li className="divider"><img src={divider} alt=""/></li>
                <li><NavLink to="../prices">&nbsp;ПРАЙС-ЛИСТ&nbsp;</NavLink></li>
                <li className="divider"><img src={divider} alt=""/></li>
                <li><NavLink to="../account">&nbsp;ЛИЧНЫЙ&nbsp;КАБИНЕТ&nbsp;</NavLink></li>
                <li className="divider"><img src={divider} alt=""/></li>
                <li><NavLink to="../contacts">&nbsp;КОНТАКТЫ&nbsp;</NavLink></li>
              </ul>
            </div>
          </div>
        </div>
      </header>
  );
}

export default Header;