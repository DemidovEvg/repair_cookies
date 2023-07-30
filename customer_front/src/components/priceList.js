import PricesList from "./price";

function Prices({prices}) {
  return (
      <div className="site-content-wrap">
        <div className="nav-background"></div>
        <div className="site-content">
          <div className="price-list-head">
            <div className="price-list-heading">ПРАЙС-ЛИСТ</div>
            <div>
              Наши цены на&nbsp;услуги по&nbsp;компьютерной помощи окончательны, то&nbsp;есть не&nbsp;включают скрытых
              надбавок, которые в&nbsp;дальнейшем могут привести к&nbsp;значительному увеличению стоимости ремонта.
              После бесплатной диагностики окончательная смета работ составляется специалистом из&nbsp;нижеуказанных цен
              плюс стоимость комплектующих в&nbsp;случае необходимости их&nbsp;замены.
            </div>
          </div>
          <div className="price-tables">
            <div className="short-price-only upper-price-part">
              <div className="short-price-row"></div>
              <div className="short-price-row"><p>Выезд курьера</p><p>бесплатно</p></div>
              <div className="short-price-row"><p>Диагностика</p><p>бесплатно</p></div>
            </div>
            <div className="price-list-small-heading">АППАРАТНАЯ ЧАСТЬ</div>
            <div className="short-price-only">
              <div className="short-price-part">РЕМОНТ ТЕЛЕФОНОВ</div>
              <PricesList
                  prices={prices}
                  category='TELEPHONE'
                  kind={['Аппаратная часть']}
                  subKind={['Электромеханический ремонт', 'Прошивка и настройка', undefined]}
              />

              <div className="short-price-part">РЕМОНТ ПЛАНШЕТОВ</div>
              <PricesList
                  prices={prices}
                  category='TABLET'
                  kind={['Аппаратная часть']}
                  subKind={['Электромеханический ремонт', 'Прошивка и настройка', undefined]}
              />

              <div className="short-price-part">РЕМОНТ НОУТБУКОВ</div>
              <PricesList
                  prices={prices}
                  category='LAPTOP'
                  kind={['Аппаратная часть']}
                  subKind={['Электромеханический ремонт', 'Прошивка и настройка', undefined]}
              />
            </div>

            <div className="price-list-small-heading">ПРОГРАММНАЯ ЧАСТЬ</div>
            <div className="short-price-only">
              <div className="short-price-part">ОПЕРАЦИОННАЯ СИСТЕМА</div>
              <PricesList
                  prices={prices}
                  category='LAPTOP'
                  kind={['Программная часть']}
                  subKind={['Операционная система']}
              />
              <div className="short-price-part">ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ</div>
              <PricesList
                  prices={prices}
                  category='LAPTOP'
                  kind={['Программная часть']}
                  subKind={['Программное обеспечение']}
              />
            </div>

            <div className="price-list-small-heading">ВОССТАНОВЛЕНИЕ ДАННЫХ</div>
            <div className="short-price-only">
              <PricesList
                  prices={prices}
                  category='LAPTOP'
                  kind={['Восстановление данных']}
                  subKind={['Электромеханический ремонт', 'Прошивка и настройка', undefined]}
              />
            </div>
          </div>
          <div className="empty-space"></div>
        </div>

      </div>
  );
}

export default Prices

