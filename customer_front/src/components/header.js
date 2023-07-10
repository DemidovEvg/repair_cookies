import logo from '../img/logo.svg';
import arrow from '../img/arrow.svg';
import icon1 from '../img/sn-icon-1.svg'
import icon2 from '../img/sn-icon-2.svg'
import divider from '../img/divider.svg'


function Header({ isAuth, logOut }) {
  return (
      <header>
        <div className="site-nav">
          <div className="logo">
            <img src={logo} alt="logo"/>
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
                <li><a className="link" href="/">ГЛАВНАЯ</a></li>
                <li className="divider"><img src={divider} alt=""/></li>
                <li><a href="/">О НАС</a></li>
                <li className="divider"><img src={divider} alt=""/></li>
                <li className="services"><a href="/">УСЛУГИ</a>
                  <ul className="dropdown">
                    <li><a href="/">Ремонт телефонов</a></li>
                    <li>
                      <hr/>
                    </li>
                    <li><a href="/">Ремонт планшетов</a></li>
                    <li>
                      <hr/>
                    </li>
                    <li><a href="/">Ремонт ноутбуков</a></li>
                  </ul>
                </li>
                <li className="divider"><img src={divider} alt=""/></li>
                <li><a href="/">ПРАЙС-ЛИСТ</a></li>
                <li className="divider"><img src={divider} alt=""/></li>
                <li><a href="/">ЛИЧНЫЙ&nbsp;КАБИНЕТ</a></li>
                <li className="divider"><img src={divider} alt=""/></li>
                <li><a href="/">КОНТАКТЫ</a></li>
              </ul>
            </div>
          </div>
        </div>
      </header>
  );
}

export default Header;