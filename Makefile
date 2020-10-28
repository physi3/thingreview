run:
	python manage.py runserver 0.0.0.0:8000

install:
	pip install -r requirements.txt

test:
	python manage.py test

collectstatic:
	python manage.py collectstatic --noinput

migrate:
	python manage.py makemigrations things
	python manage.py makemigrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser
