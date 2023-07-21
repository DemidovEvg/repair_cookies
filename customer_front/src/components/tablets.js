import one from '../img/1.svg'
import two from '../img/2.svg'
import three from '../img/3.svg'
import four from '../img/4.svg'
import {NavLink} from "react-router-dom";

function Tablets() {
  return (
      <div className="site-content-wrap">
        <div className="nav-background"></div>
        <div className="site-content">
          <div className="repair-details-head">
            <div className="repair-details-header">
              <img className="repair-details-icon" src={require("../img/tablet.svg")} alt="" />
                <p className="white-big-text">РЕМОНТ ПЛАНШЕТОВ</p>
            </div>
          </div>
          <div className="about-device-wrap">
            <div className="about-device">
              <div className="simple-black-text">
                <p>
                  Планшеты – достаточно хрупкая техника, которая легко выходит из строя от механических
                  повреждений. Уронив гаджет или нечаянно сев на него, вы с большой долей вероятности
                  получите треснутое стекло дисплея или повреждение матрицы экрана.
                </p>
                <hr/>
              </div>
              <div className="reasons-and-picture">
                <div className="picture-from-reasons">
                  <img src={require("../img/tablet_details.jpg")} alt="" />
                </div>
              </div>
              <div className="reason-heading">
                <hr/>
                  <p>
                    ВЫШЕДШИЕ ИЗ СТРОЯ КОМЛЕКТУЮЩИЕ ПЛАНЩЕТА ОБЫЧНО ТРЕБУЮТ НЕМАЛЫХ ЗАТРАТ НА ВОССТАНОВЛЕНИЕ,
                    ТАК КАК ВСЕ ОСНОВНЫЕ МИКРОСХЕМЫ ГАДЖЕТОВ НЕ ОТНОСЯТСЯ К КАТЕГОРИИ ЗАПЧАСТЕЙ. ИХ НУЖНО
                    ИЛИ РЕМОНТИРОВАТЬ, ИЛИ ПОКУПАТЬ НОВОЕ УСТРОЙСТВО.
                  </p>
              </div>
              <div className="simple-black-text">
                <hr/>
                  <p>
                    Планшеты разных брендов имеют разные типы поломок, здесь потребуется высокая
                    квалификация специалистов, огромный опыт и своевременное обращение в компьютерный
                    сервис. Наш сервисный центр СМАРТ РЕМОНТ готов предложить вам ремонт планшетов различных
                    производителей: Apple, Asus, HP, Sony, Lenovo, Acer и других. Наши специалисты
                    гарантируют надлежащее исполнение заявленных работ, установку исключительно оригинальных
                    комплектующих и срочную помощь в восстановлении работы моноблока.
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
                      <img src={one} alt="1" />
                        <p>Для вызова специалиста оформите заявку на&nbsp;нашем сайте или
                          по&nbsp;телефону, обязательно укажите марку и&nbsp;модель устройства,
                          подробно опишите проблему: это даст возможность специалисту подготовить
                          нужные детали и&nbsp;инструменты для ремонта.</p>
                    </li>
                    <li>
                      <img src={two} alt="2" />
                        <p>Наш специалист прибудет по&nbsp;указанному адресу в&nbsp;течение часа, или
                          вы&nbsp;можете договориться о&nbsp;любом удобном для вас времени.</p>
                    </li>
                    <li>
                      <img src={three} alt="3" />
                        <p>Мастер бесплатно проведет диагностику вашего компьютера для выявления причины
                          неисправности, предложит перечень необходимых работ и&nbsp;согласует
                          с&nbsp;вами стоимость ремонта.</p>
                    </li>
                    <li>
                      <img src={four} alt="4" />
                        <p>Мастер проведет работы по&nbsp;ремонту и&nbsp;настройке вашего компьютера.
                          По&nbsp;окончании работ подписывается договор и&nbsp;акт выполненных работ
                          с&nbsp;предоставлением гарантии на&nbsp;выполненные работы
                          и&nbsp;комплектующие сроком на&nbsp;1&nbsp;год.</p>
                    </li>
                  </ul>
                </div>
              </div>
              <NavLink className="form-bringer" to="../repair">ВЫЗВАТЬ КУРЬЕРА</NavLink>
            </div>
          </div>
          <div className="short-price-for-cathegory-wrap">
            <div className="short-price-for-cathegory">
              <div className="short-price-header-hr">
                <p>СТОИМОСТЬ РАБОТ</p>
                <hr />
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
                <div className="short-price-row">
                  <p>Замена дисплея</p>
                  <p>1800 руб.</p>
                </div>
                <div className="short-price-row">
                  <p>Замена кнопки включения</p>
                  <p>150 руб.</p>
                </div>
                <div className="short-price-row">
                  <p>Ремонт микрофона</p>
                  <p>300 руб.</p>
                </div>
                <div className="short-price-row">
                  <p>Замена динамика</p>
                  <p>480 руб.</p>
                </div>
                <div className="short-price-row">
                  <p>Попадание воды</p>
                  <p>900 руб.</p>
                </div>
                <div className="short-price-row">
                  <p>Смена корпуса</p>
                  <p>999 руб.</p>
                </div>
                <div className="short-price-row">
                  <p>Ремонт передатчика</p>
                  <p>3700 руб.</p>
                </div>
                <div className="short-price-row">
                  <p>Не видит сим-карту</p>
                  <p>50 руб.</p>
                </div>
                <div className="short-price-row">
                  <p>Проблема с зарядкой</p>
                  <p>150 руб.</p>
                </div>
                <div className="short-price-part">ПРОГРАММНАЯ ЧАСТЬ</div>
                <div className="short-price-row">
                  <p>Смена версии ПО</p>
                  <p>БЕСПЛАТНО</p>
                </div>
                <div className="short-price-row">
                  <p>Восстановление данных</p>
                  <p>БЕСЦЕННО</p>
                </div>
              </div>
              <NavLink className="form-bringer" to="../prices">ПОЛНЫЙ ПРАЙС-ЛИСТ</NavLink>
            </div>
          </div>
        </div>
      </div>
  );
}

export default Tablets