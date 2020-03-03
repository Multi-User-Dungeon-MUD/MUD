web: gunicorn adv_project.wsgi:application --log-file -
release: python3 ./manage.py makemigrations
release: python3 ./manage.py migrate