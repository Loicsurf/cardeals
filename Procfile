web: gunicorn cardeal.wsgi --preload --log-file -
python manage.py collectstatic --noinput
manage.py migrate
