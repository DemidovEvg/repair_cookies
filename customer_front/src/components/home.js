import phone from '../img/phone.svg';
import notebook from '../img/notebook.svg';
import tablet from '../img/tablet.svg';
import percent from '../img/percent.svg';
import wallet from '../img/wallet.svg';
import letter from '../img/letter-1.svg';
import groupPro from '../img/group-pro.svg';
import upgrade from '../img/Upgrade.svg';
import laptopClock from '../img/laptop-clock.svg';
import biBoxSeam from '../img/bi_box-seam.svg';
import winLogo from '../img/win-logo.svg';
import talkingCouple from '../img/talking-couple.svg';
import {NavLink} from "react-router-dom";

function Home() {
  return (
      <div className="site-content-wrap">
        <div className="background-img"><img src={require('../img/background_strings.jpg')} alt=""/></div>
        <div className="main-page-top">
          <div className="main-text-block">
            <p className="the-biggest-font text-to-style-orange">ОПЕРАТИВНЫЙ<br/>РЕМОНТ<br/>ГАДЖЕТОВ</p>
            <p className="small-white-text text-to-style">Ремонт любой сложности телефонов, планшетов<br/>и ноутбуков
            </p>
            <p className="small-orange-text text-to-style-orange">Срочный выезд курьера</p>
            <NavLink className="form-bringer" to="../repair">ХОЧУ РЕМОНТ</NavLink>
          </div>
          <div className="guy-with-laptop">
            <img className="quy-closer" src={require('../img/Man note 1.png')} alt=""/>
          </div>
        </div>
        <div className="block-service">
          <div className="repair-card">
            <div className="top-card">
              <img src={phone} alt=""/>
            </div>
            <div className="card-heading">РЕМОНТ ТЕЛЕФОНОВ</div>
            <div className="card-list">
              <ul>
                <li className="marked">Замена дисплея (ремонт экрана)</li>
                <li className="marked">Смена корпуса</li>
                <li className="marked">Ремонт микрофона</li>
                <li className="marked">Ремонт динамика</li>
                <li className="marked">Проблемы с зарядкой</li>
                <li className="marked">Попадание воды</li>
                <li>и другое...</li>
              </ul>
            </div>
            <NavLink className="price-list-link" to="../services/phones">ПОДРОБНОСТИ И ЦЕНЫ</NavLink>
          </div>
          <div className="repair-card">
            <div className="top-card">
              <img src={notebook} alt=""/>
            </div>
            <div className="card-heading">РЕМОНТ НОУТБУКОВ</div>
            <div className="card-list">
              <ul>
                <li className="marked">Ремонт залитого ноутбука</li>
                <li className="marked">Замена клавиатуры</li>
                <li className="marked">Замена экрана</li>
                <li className="marked">Замена термопасты</li>
                <li className="marked">Чистка от пыли</li>
                <li className="marked">Замена жесткого диска</li>
                <li> и другое...</li>
              </ul>
            </div>
            <NavLink className="price-list-link" to="../services/notebooks">ПОДРОБНОСТИ И ЦЕНЫ</NavLink>
          </div>
          <div className="repair-card">
            <div className="top-card">
              <img src={tablet} alt=""/>
            </div>
            <div className="card-heading">РЕМОНТ ПЛАНШЕТОВ</div>
            <div className="card-list">
              <ul>
                <li className="marked">Замена дисплея (ремонт экрана)</li>
                <li className="marked">Смена корпуса</li>
                <li className="marked">Ремонт микрофона</li>
                <li className="marked">Ремонт динамика</li>
                <li className="marked">Проблемы с зарядкой</li>
                <li className="marked">Попадание воды</li>
                <li>и другое...</li>
              </ul>
            </div>
            <NavLink className="price-list-link" to="../services/tablets">ПОДРОБНОСТИ И ЦЕНЫ</NavLink>
          </div>
        </div>
        <div className="call-courier-wrap">
          <div className="call-courier">
            <p className="big-font">НУЖЕН РЕМОНТ ТЕХНИКИ?</p>
            <hr/>
            <div className="call-steps-block">
              <div className="call-img">
                <img src={require('../img/call-us.jpg')} alt=""/>
              </div>
              <div className="list-style-count">
                <ul>
                  <li>
                    <button className="list-style-count">1</button>
                  </li>
                  <li>
                    <button className="list-style-count">2</button>
                  </li>
                  <li>
                    <button className="list-style-count">3</button>
                  </li>
                  <li>
                    <button className="list-style-count">4</button>
                  </li>
                </ul>
              </div>


              <div className="call-steps">
                <ul>
                  <li>Вызовите курьера в удобное для вас время</li>
                  <li>Узнайте причину неисправности, перечень необходимых работ и стоимость ремонта</li>
                  <li>Платите по окончанию выполнения ремонта и подписания договора</li>
                  <li>Получите гарантию 1 год на произведенные работы</li>
                </ul>
              </div>
            </div>
            <hr/>
          </div>
        </div>
        <div className="why-us">
          <p className="big-font">ПОЧЕМУ СТОИТ ОБРАТИТЬСЯ К НАМ</p>
          <hr/>
          <div className="why-us-cards">
            <div className="row-cards">
              <div className="one-of-nine">
                <img src={percent} alt=""/>
                <p>РЕМОНТНЫХ РАБОТ ВЫПОЛНЯЮТСЯ ОТ&nbsp;ОДНОГО ДО&nbsp;ТРЕХ ДНЕЙ</p>
              </div>
              <div className="one-of-nine">
                <img src={wallet} alt=""/>
                <p>ДЕМОКРАТИЧНЫЕ ЦЕНЫ, ОТСТУТСТВИЕ СКРЫТЫХ УСЛУГ И&nbsp;ДОПЛАТ</p>
              </div>
              <div className="one-of-nine">
                <img src={letter} alt=""/>
                <p>ГАРАНТИЯ НА&nbsp;РЕМОНТНЫЕ РАБОТЫ И&nbsp;КОМПЛЕКТУЮЩИЕ ОДИН&nbsp;ГОД</p>
              </div>
            </div>
            <div className="row-cards">
              <div className="one-of-nine">
                <img src={groupPro} alt=""/>
                <p>ВСЕ МАСТЕРА&nbsp;&mdash;ДИПЛОМИРОВАННЫЕ СПЕЦИАЛИСТЫ С ОПЫТОМ РАБОТЫ БОЛЕЕ 8 ЛЕТ </p>
              </div>
              <div className="one-of-nine">
                <img src={upgrade} alt=""/>
                <p>СОВРЕМЕННОЕ ПРОФЕССИОНАЛЬНОЕ ОБОРУДОВАНИЕ ДЛЯ&nbsp;ДИАГНОСТИКИ И&nbsp;РЕМОНТА</p>
              </div>
              <div className="one-of-nine">
                <img src={laptopClock} alt=""/>
                <p>ПРИ&nbsp;НЕОБХОДИМОСТИ ПРОВЕДЕМ РЕМОНТ ВЕЧЕРОМ ИЛИ&nbsp;ДНЁМ</p>
              </div>
            </div>
            <div className="row-cards">
              <div className="one-of-nine">
                <img src={biBoxSeam} alt=""/>
                <p>ВСЕ ЗАПЧАСТИ ТОЛЬКО&nbsp;ОТ ОФИЦИАЛЬНЫХ ДИСТРИБЬЮТОРОВ</p>
              </div>
              <div className="one-of-nine">
                <img src={winLogo} alt=""/>
                <p>ЛИЦЕНЗИОННЫЕ КЛЮЧИ&nbsp;НА ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПО&nbsp;ОПТОВОЙ ЦЕНЕ</p>
              </div>
              <div className="one-of-nine">
                <img src={talkingCouple} alt=""/>
                <p>9 ИЗ 10 ОБРАТИВШИХСЯ РЕКОМЕНДУЮТ&nbsp;НАС ДРУЗЬЯМ И&nbsp;ЗНАКОМЫМ</p>
              </div>
            </div>
          </div>
        </div>
      </div>

  );
}

export default Home;