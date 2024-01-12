FROM python:3.8.2-buster

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_USERNAME "admin"
ENV DJANGO_SUPERUSER_EMAIL "admin@instamojo.com"
ENV DJANGO_SUPERUSER_PASSWORD "admin@123"

ARG DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install -y python

ARG ENV_TYPE
ENV ENV_TYPE=$ENV_TYPE

COPY requirements/ /requirements/
RUN pip install --upgrade pip
RUN pip install -r /requirements/requirements.txt

COPY ./compose/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

ADD . /app/

WORKDIR /app