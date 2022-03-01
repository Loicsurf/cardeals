web: gunicorn cardeal.wsgi --preload --log-file  - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
