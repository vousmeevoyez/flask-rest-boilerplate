clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

tests:
	python manage.py test

run:
	python manage.py run

coverage:
	coverage run --source app/api -m unittest discover -s app/tests/
