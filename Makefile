debug:
	FLASK_APP=app.py \
	FLASK_ENV=development \
	python3 -m src

pytest:
	poetry run pytest src tests/

cov-check:
	poetry run pytest --cov=src tests/