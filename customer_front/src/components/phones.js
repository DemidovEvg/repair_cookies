import phone from '../img/phone.svg'
import one from '../img/1.svg'
import two from '../img/2.svg'
import three from '../img/3.svg'
import four from '../img/4.svg'
import PricesList from "./price";
import {NavLink} from "react-router-dom";

function Phones({prices}) {
  return (
      <div className="site-content-wrap">
        <div className="nav-background"></div>
        <div className="site-content">
          <div className="repair-details-head">
            <div className="repair-details-header">
              <img className="repair-details-icon" src={phone} alt=""/>
              <p className="white-big-text">РЕМОНТ ТЕЛЕФОНОВ</p>
            </div>
          </div>
          <div className="about-device-wrap">
            <div className="about-device">
              <div className="simple-black-text">
                <p>
                  Современные смартфоны и мобильные телефоны можно защитить от повреждений, например,
                  купить чехол и наклеить бронестекло на экран. Тем не менее, даже в этом случае их можно
                  повредить: уронить на асфальт, бетон или кафельный пол.
                </p>
                <p>
                  Если вы уронили свой телефон в воду или пролили на него воду, в первую очередь выключите
                  устройство и извлеките из него аккумулятор. Доверьте свой гаджет нам, после диагностики
                  мы точно скажем, есть ли необходимость в ремонте и сколько это будет стоить.
                </p>
                <hr/>
              </div>
              <div className="reasons-and-picture">
                <div className="picture-from-reasons">
                  <img src={require('../img/telephone_details.jpg')} alt=""/>
                </div>
              </div>
              <div className="reason-heading">
                <hr/>
                <p>
                  ВЫСОКАЯ КВАЛИФИКАЦИЯ МАСТЕРОВ И СПЕЦИАЛЬНОЕ ОБОРУДОВАНИЕ ДЛЯ ДИАГНОСТИКИ, КОМПОНЕНТНОГО
                  И МОДУЛЬНОГО РЕМОНТА ПОЗВОЛЯЕТ НАМ ВОССТАНАВЛИВАТЬ ТЕЛЕФОНЫ ЛЮБОЙ МОДЕЛИ
                </p>
              </div>
            </div>
          </div>
          <div className="repair-details-1-2-3-4-wrap">
            <div className="repair-details-1-2-3-4">
              <div className="head-and-hr-1-2-3-4">
                <p>Компьютерный сервис СМАРТ РЕМОНТ предоставляет услугу срочного выездного ремонта
                  компьютерной техники в Москве и МО</p>
                <hr/>
              </div>
              <div className="only-details-1-2-3-4">
                <div className="text-1-2-3-4">
                  <ul>
                    <li>
                      <img src={one} alt="1"/>
                      <p>Для вызова специалиста оформите заявку на&nbsp;нашем сайте или
                        по&nbsp;телефону, обязательно укажите марку и&nbsp;модель устройства,
                        подробно опишите проблему: это даст возможность специалисту подготовить
                        нужные детали и&nbsp;инструменты для ремонта.</p>
                    </li>
                    <li>
                      <img src={two} alt="2"/>
                      <p>Наш специалист прибудет по&nbsp;указанному адресу в&nbsp;течение часа, или
                        вы&nbsp;можете договориться о&nbsp;любом удобном для вас времени.</p>
                    </li>
                    <li>
                      <img src={three} alt="3"/>
                      <p>Мастер бесплатно проведет диагностику вашего компьютера для выявления причины
                        неисправности, предложит перечень необходимых работ и&nbsp;согласует
                        с&nbsp;вами стоимость ремонта.</p>
                    </li>
                    <li>
                      <img src={four} alt="4"/>
                      <p>Мастер проведет работы по&nbsp;ремонту и&nbsp;настройке вашего компьютера.
                        По&nbsp;окончании работ подписывается договор и&nbsp;акт выполненных работ
                        с&nbsp;предоставлением гарантии на&nbsp;выполненные работы
                        и&nbsp;комплектующие сроком на&nbsp;1&nbsp;год.</p>
                    </li>
                  </ul>
                </div>
              </div>
              <NavLink to="/repair" className="form-bringer">ВЫЗВАТЬ КУРЬЕРА</NavLink>
            </div>
          </div>
          <div className="short-price-for-cathegory-wrap">
            <div className="short-price-for-cathegory">
              <div className="short-price-header-hr">
                <p>СТОИМОСТЬ РАБОТ</p>
                <hr/>
              </div>
              <div className="simple-black-text">
                <p>
                  Наши цены на&nbsp;услуги по&nbsp;ремонту ноутбуков окончательны, то&nbsp;есть
                  не&nbsp;включают скрытых надбавок, которые в&nbsp;дальнейшем могут привести
                  к&nbsp;значительному увеличению стоимости ремонта. После бесплатной диагностики
                  окончательная смета работ составляется из&nbsp;нижеуказанных цен плюс стоимость
                  комплектующих в&nbsp;случае необходимости их&nbsp;замены.
                </p>
              </div>
              <div className="short-price-only">
                <div className="short-price-part">АППАРАТНАЯ ЧАСТЬ</div>

                <PricesList
                    prices={prices}
                    category='TELEPHONE'
                    kind={['Аппаратная часть']}
                    subKind={['Электромеханический ремонт', undefined]}
                />


                <div className="short-price-part">ПРОГРАММНАЯ ЧАСТЬ</div>
                <PricesList
                    prices={prices}
                    category='TELEPHONE'
                    kind={['Программная часть']}
                    subKind={['Прошивка и настройка', undefined]}
                />
              </div>
              <NavLink className="form-bringer" to="/prices">ПОЛНЫЙ ПРАЙС-ЛИСТ</NavLink>
            </div>
          </div>
        </div>
      </div>
  );
}

export default Phones