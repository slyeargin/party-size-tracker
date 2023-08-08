# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm

COPY ./requirements.txt /api/requirements.txt
WORKDIR /api
RUN pip3 install -r requirements.txt

COPY ./api /api

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=81"]