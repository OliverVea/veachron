# syntax=docker/dockerfile:1

FROM python:3.10.7-bullseye

WORKDIR /usr/src/app

RUN apt-get update
#RUN apt-get -y install libpq-dev python-dev gcc
RUN pip install --upgrade pip
COPY ./veachron/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY veachron ./veachron

CMD [ "python3", "-m", "veachron" ]