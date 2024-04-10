#!/bin/bash

sleep 3

python manage.py migrate

if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --noinput \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py collectstatic --noinput
gunicorn settings.wsgi:application --bind 0.0.0.0:8000

exec "$@"
