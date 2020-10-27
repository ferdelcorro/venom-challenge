FROM python:3.8.3-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN apt-get update && apt-get install
RUN pip3 install -r requirements.txt
COPY . /code/