FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV MYAPI_VERSION 0.1
ENV STATIC_URL /static
ENV STATIC_PATH ./app/static
COPY ./  /app/
COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install -r /var/www/requirements.txt