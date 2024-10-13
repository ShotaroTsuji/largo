FROM python:3.10.1-slim as build

ARG APP=/usr/app

RUN apt-get update \
 && apt-get install -y build-essential ledger \
 && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip poetry

RUN mkdir -p ${APP}
WORKDIR ${APP}

ADD . ./

RUN poetry config virtualenvs.in-project true \
 && poetry install --no-interaction

ENV PATH=${APP}/.venv/bin:$PATH
WORKDIR /home/largo
