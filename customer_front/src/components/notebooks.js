import notebook from '../img/notebook.svg'
import one from '../img/1.svg'
import two from '../img/2.svg'
import three from '../img/3.svg'
import four from '../img/4.svg'
import philips from '../img/Philips.svg';
import apple from '../img/Apple.svg';
import toshiba from '../img/Toshiba.svg';
import hp from '../img/HP.svg';
import lenovo from '../img/Lenovo.svg';
import xiaomi from '../img/Xiaomi.svg';
import huawei from '../img/Huawei.svg';
import lg from '../img/LG.svg';
import sony from '../img/Sony.svg';
import dell from '../img/Dell.svg';
import samsung from '../img/Samsung.svg';
import asus from '../img/Asus.svg';
import vaio from '../img/Vaio.svg';
import acer from '../img/Acer.svg';
import PricesList from "./price";
import {NavLink} from "react-router-dom";

function Notebooks({prices}) {
  return (
      <div className="site-content-wrap">
        <div className="nav-background"></div>
        <div className="site-content">
          <div className="repair-details-head">
            <div className="repair-details-header">
              <img className="repair-details-icon" src={notebook} alt=""/>
              <p className="white-big-text">РЕМОНТ НОУТБУКОВ</p>
            </div>
          </div>
          <div className="about-device-wrap">
            <div className="about-device">
              <div className="simple-black-text">
                <p>
                  Благодаря своей мобильности и&nbsp;компактности ноутбуки в&nbsp;современном мире стали одним
                  из&nbsp;самых востребованных видов компьютерной техники, но, к&nbsp;сожалению, они, наиболее часто
                  подвержены разного рода поломкам. В&nbsp;отличие от&nbsp;стационарного компьютера, где поломки носят
                  обычно локальный характер, например, сломалась клавиатура или вышел из&nbsp;строя монитор,
                  в&nbsp;ноутбуке, из-за его комплексной конструкции, велик риск выхода из&nbsp;строя сразу всего
                  аппарата.
                </p>
                <p>
                  Независимо от&nbsp;того, какой модели у&nbsp;вас ноутбук, он&nbsp;может выйти из&nbsp;строя
                  по&nbsp;следующим причинам:
                </p>
                <hr/>
              </div>
              <div className="reasons-and-picture">
                <div className="text-from-reasons">
                  <p className="reason-heading">ЗАВОДСКОЙ БРАК</p>
                  <p>
                    Если изначально в&nbsp;девайсе установлены бракованные комплектующие, они не&nbsp;выдержат нагрузки,
                    и&nbsp;техника начнет работать со&nbsp;сбоями.
                  </p>
                  <p className="reason-heading">ДЛИТЕЛЬНАЯ ЭКСПЛУАТАЦИЯ</p>
                  <p>
                    Компоненты системы с&nbsp;течением времени подвергаются износу, ломаются. Поэтому какие-либо
                    элементы может потребоваться заменить.
                  </p>
                  <p className="reason-heading"> НАРУШЕНИЕ ПРАВИЛ ЭКСПЛУАТАЦИИ</p>
                </div>
                <div className="picture-from-reasons">
                  <img src={require("../img/laptop-iside.jpg")} alt=""/>
                </div>
              </div>
              <div className="simple-black-text">
                <hr/>
                <p>
                  Расколотые корпуса, облитая жидкостью клавиатура. самопроизвольное отключение, сбой батарей,
                  перегрев вентилятора, торможения (зависание оборудования), искаженное изображение
                  на&nbsp;экране&nbsp;&mdash; это основные, но&nbsp;далеко не&nbsp;все проблемы, с&nbsp;которыми
                  обращаются в&nbsp;наш компьютерный сервис.
                  Какой&nbsp;бы ни&nbsp;была поломка вашего ноутбука, обратитесь в&nbsp;сервис СМАРТ РЕМОНТ. Наши
                  мастера окажут срочную профессиональную помощь и&nbsp;вернут ваш ноутбук к&nbsp;жизни
                  с&nbsp;гарантией стабильной безотказной работы при условии правильной эксплуатации. В&nbsp;90%
                  случаев с&nbsp;проблемой удается справиться в&nbsp;день обращения, при серьезных проблемах
                  неисправное устройство будет бесплатно доставлено в&nbsp;сервисный центр.
                </p>
              </div>
            </div>
          </div>
          <div className="repair-details-1-2-3-4-wrap">
            <div className="repair-details-1-2-3-4">
              <div className="head-and-hr-1-2-3-4">
                <p>Компьютерный сервис СМАРТ РЕМОНТ предоставляет услугу срочного выездного ремонта компьютерной техники
                  в Москве и МО</p>
                <hr/>
              </div>
              <div className="only-details-1-2-3-4">
                <div className="text-1-2-3-4">
                  <ul>
                    <li>
                      <img src={one} alt="1"/><p>Для вызова специалиста оформите заявку на&nbsp;нашем сайте или
                      по&nbsp;телефону, обязательно укажите марку и&nbsp;модель устройства, подробно опишите проблему:
                      это даст возможность специалисту подготовить нужные детали и&nbsp;инструменты для ремонта.</p>
                    </li>
                    <li>
                      <img src={two} alt="2"/><p>Наш специалист прибудет по&nbsp;указанному адресу в&nbsp;течение
                      часа, или вы&nbsp;можете договориться о&nbsp;любом удобном для вас времени.</p>
                    </li>
                    <li>
                      <img src={three} alt="3"/><p>Мастер бесплатно проведет диагностику вашего компьютера для
                      выявления причины неисправности, предложит перечень необходимых работ и&nbsp;согласует
                      с&nbsp;вами стоимость ремонта.</p>
                    </li>
                    <li>
                      <img src={four} alt="4"/><p>Мастер проведет работы по&nbsp;ремонту и&nbsp;настройке вашего
                      компьютера. По&nbsp;окончании работ подписывается договор и&nbsp;акт выполненных работ
                      с&nbsp;предоставлением гарантии на&nbsp;выполненные работы и&nbsp;комплектующие сроком
                      на&nbsp;1&nbsp;год.</p>
                    </li>
                  </ul>
                </div>
              </div>
              <NavLink className="form-bringer" to="/repair">ВЫЗВАТЬ КУРЬЕРА</NavLink>
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
                  Наши цены на&nbsp;услуги по&nbsp;ремонту ноутбуков окончательны, то&nbsp;есть не&nbsp;включают скрытых
                  надбавок, которые в&nbsp;дальнейшем могут привести к&nbsp;значительному увеличению стоимости ремонта.
                  После бесплатной диагностики окончательная смета работ составляется из&nbsp;нижеуказанных цен плюс
                  стоимость комплектующих в&nbsp;случае необходимости их&nbsp;замены.
                </p>
              </div>
              <div className="short-price-only">
                <div className="short-price-part">АППАРАТНАЯ ЧАСТЬ</div>
                <PricesList
                    prices={prices}
                    category='LAPTOP'
                    kind={['Аппаратная часть']}
                    subKind={['Электромеханический ремонт', 'Прошивка и настройка']}
                />
                <PricesList
                    prices={prices}
                    category='LAPTOP'
                    kind={['Программная часть']}
                    subKind={['Операционная система', 'Программное обеспечение']}
                />
              </div>
              <NavLink className="form-bringer" to="/prices">ПОЛНЫЙ ПРАЙС-ЛИСТ</NavLink>
            </div>
            <div className="we-fix-everything">
              <div className="we-fix-everything-head">МЫ&nbsp;РЕМОНТИРУЕМ НОУТБУКИ ЛЮБЫХ МАРОК И&nbsp;УСТРАНЯЕМ
                НЕИСПРАВНОСТИ ЛЮБОЙ СЛОЖНОСТИ
              </div>
              <div className="we-fix-everything-icons">
                <hr/>
                <img src={philips} alt=""/>
                <img src={apple} alt=""/>
                <img src={toshiba} alt=""/>
                <img src={hp} alt=""/>
                <img src={lenovo} alt=""/>
                <img src={xiaomi} alt=""/>
                <img src={huawei} alt=""/>
                <img src={lg} alt=""/>
                <img src={sony} alt=""/>
                <img src={dell} alt=""/>
                <img src={samsung} alt=""/>
                <img src={asus} alt=""/>
                <img src={vaio} alt=""/>
                <img src={acer} alt=""/>
                <hr/>
              </div>
              <p>В&nbsp;СВОЕЙ РАБОТЕ МЫ&nbsp;ИСПОЛЬЗУЕМ ТОЛЬКО ЛИЦЕНЗИОННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ И&nbsp;ОРИГИНАЛЬНЫЕ
                КОМПЛЕКТУЮЩИЕ ОТ&nbsp;ОФИЦИАЛЬНЫХ ДИСТРИБЬЮТОРОВ</p>
            </div>
          </div>
        </div>
      </div>
  );
}

export default Notebooks