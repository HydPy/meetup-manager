cd meetup_manager/

pipenv run python manage.py makemigrations
pipenv run python manage.py migrate --no-input
pipenv run python manage.py collectstatic --no-input --clear

pipenv run gunicorn meetup_manager.wsgi:application --bind 0.0.0.0:8000 -w 4 --log-file -
