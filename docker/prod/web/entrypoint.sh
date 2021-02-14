#!/bin/sh
# shellcheck disable=SC2086

echo "Waiting for postgres..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done
echo "PostgreSQL started"


python manage.py check --deploy
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py makemessages --all
gunicorn src.wsgi:application --bind 0.0.0.0:8000 --reload
exec "$@"
