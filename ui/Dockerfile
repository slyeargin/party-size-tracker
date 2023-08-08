# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm

COPY ./requirements.txt /ui/requirements.txt
WORKDIR /ui
RUN pip3 install -r requirements.txt

COPY ./ui /ui

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]