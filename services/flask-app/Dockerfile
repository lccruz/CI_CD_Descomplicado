FROM python:3.12.4-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY src /code/src

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 src.app:app
