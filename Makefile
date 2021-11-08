# This file is part of Oasis
# https://github.com/znhv/censor

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2021 Boris Zhenikhov

run-playbook:
	ansible-playbook -i production.ini -u ubuntu playbook.yaml

up:
	docker-compose up -d

down:
	docker-compose down


debug:
	FLASK_APP=app.py \
	FLASK_ENV=development \
	python3 -m src

install:
	@poetry install
	@poetry build
	python3 -m pip install dist/*.whl --force-reinstall

clean:
	@rm -rf build dist .eggs *.egg-info
	@rm -rf .benchmarks .coverage coverage.xml htmlcov report.xml .tox
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +

format: clean
	@poetry run black src/ tests/

test:
	make pytest
	make pytest-cov

pytest:
	poetry run pytest src tests/

cov-check:
	poetry run pytest --cov=src tests/

pytest-cov:
	@poetry run pytest --cov=src --cov-config .coveragerc tests/ -sq --cov-report xml