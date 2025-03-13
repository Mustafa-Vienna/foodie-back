release: python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn foodie_api.wsgi