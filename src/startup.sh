cd meetup_manager/

pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run gunicorn meetup_manager.wsgi:application --bind 0.0.0.0:8080
