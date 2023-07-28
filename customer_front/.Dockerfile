FROM base_front
WORKDIR /usr/src/app

COPY customer_front/public /usr/src/app/public 
COPY customer_front/src /usr/src/app/src 