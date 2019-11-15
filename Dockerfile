FROM alpine:3.10

RUN apk add --update python3 py-pip postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /src/requirements.txt

WORKDIR /scr

RUN pip3 install -r /src/requirements.txt

COPY . /src/