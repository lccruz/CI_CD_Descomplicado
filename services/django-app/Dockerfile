FROM python:3.12.2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc cron\
    && pip install psycopg2

RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

COPY . /code/

ENTRYPOINT ["/code/entrypoint.sh"]