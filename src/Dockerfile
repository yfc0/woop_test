# pull official base image
from python:3.9.5-slim-buster

# set work directory
workdir /usr/src/app

ENV FLASK_APP netflix.py
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade cython
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .
