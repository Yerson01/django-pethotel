FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
    gcc libc-dev linux-headers postgresql-dev libffi-dev \
    musl-dev zlib zlib-dev

RUN mkdir /app
WORKDIR /app
COPY ./Pipfile /app/Pipfile

RUN pip3 install --upgrade pip
RUN pip3 install pip-tools pipfile-requirements
RUN pipfile2req > requirements.txt \
    && pipfile2req --dev >> requirements.txt \
    && pip3 install -r requirements.txt

RUN apk del .temp-build-deps

COPY . /app

RUN adduser -D user
USER user