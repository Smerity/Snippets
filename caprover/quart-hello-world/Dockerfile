FROM python:3.7-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY app/requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

COPY app/ /app
WORKDIR /app

EXPOSE 80

CMD hypercorn -b 0.0.0.0:80 server:app
