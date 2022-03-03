FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY . /app

RUN apk add --update --no-cache --virtual .build-deps g++ gcc libxml2-dev libxslt-dev python3-dev && \
    apk add --no-cache libxslt && \
    apk add --no-cache mariadb-dev git
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg # pillow dependencies

RUN pip3.8 install -r requirements.txt
RUN apk del .build-deps
