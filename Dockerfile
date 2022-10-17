# syntax=docker/dockerfile:1

FROM python:3.10.7-slim-bullseye

WORKDIR /usr/src/app

COPY ./src/veachron/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app/src
COPY ./src/veachron .

CMD [ "python3", "-m", "veachron" ]