web: gunicorn cardeal.wsgi:application --preload --log-file -
python manage.py collectstatic --noinput
manage.py migrate
