## remove all build, test, coverage and Python artifacts
clean: clean-build clean-pyc clean-test

## remove build artifacts
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

## remove Python file artifacts
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

## remove test and coverage artifacts
clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

format:
	black app/

lint:
	python3.10 -m flake8 app/

tests: lint
	python3.10 -m pyted st -vv --cov=. --cov-report=html

run:
	python3.10 app/run.py

run-server:
	python3.10 app/run_server.py

run-client:
	python3.10 app/run_client.py

# run-game:
# 	python3.10 app/server/run.py & python3.10 app/client/run.py 1200 0 & python3.10 app/client/run.py 2200 0
