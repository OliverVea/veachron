# syntax=docker/dockerfile:1

FROM python:3.10.7-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "src/veachron/main.py" ]