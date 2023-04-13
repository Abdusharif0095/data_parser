FROM snakepacker/python:all as builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt
