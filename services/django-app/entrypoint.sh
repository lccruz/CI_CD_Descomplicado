#!/bin/sh

set -e

if [ "$1" = "web" ]; then
    gunicorn --bind :8000 --workers 1 --threads 8 --timeout 0 invista.wsgi:application
fi

if [ "$1" = "migrate" ]; then
    python manage.py showmigrations
    python manage.py migrate
fi
