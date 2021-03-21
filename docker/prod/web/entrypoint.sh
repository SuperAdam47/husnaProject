#!/bin/sh

python manage.py wait_for_db

python manage.py check --deploy
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

gunicorn -w 2 -k uvicorn.workers.UvicornH11Worker src.asgi:application --reload --bind 0.0.0.0:8000 --log-level info
# gunicorn src.wsgi:application --bind 0.0.0.0:8000 --reload
exec "$@"
