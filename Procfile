web: gunicorn adv_project.wsgi:application --log-file -
release: python3 ./manage.py makemigrations
release: python3 ./manage.py migrate
release: python3 ./manage.py util/create_world.py