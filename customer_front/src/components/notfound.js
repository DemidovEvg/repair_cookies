import notFound from '../img/404.svg'
function NotFound404() {
  return (
      <div className="site-content-wrap">
        <div className="nav-background"></div>
        <div className="site-content">

          <div className="picture-404">
            <img src={notFound} alt="Страница по адресу не найдена"/>
          </div>
        </div>
      </div>
  );
}

export default NotFound404
