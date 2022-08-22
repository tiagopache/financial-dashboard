# these will speed up builds, for docker-compose >= 1.25
SHELL := /bin/bash

export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

test: lint
	pytest -vv

unit-tests: lint
	pytest -vv ./tests/unit

integration-tests: lint
	pytest -vv ./tests/integration

e2e-tests: lint
	pytest -vv ./tests/e2e

lint:
	flake8 --exclude=.tox,*.egg,venv,.venv,build,data --ignore=W291,E303,E501 --select=E,W,F  .

code-coverage:
	pytest -vv --junitxml=unittestresults.xml --cov --cov-report=term-missing

pkg-clean: 
	rm -Rf ./build; rm -Rf ./dist; rm -Rf ./.tox; rm -Rf ./.eggs; rm -Rf ./.pytest_cache; rm -Rf ./**/*.egg-info; rm -Rf ./**/version.py; rm -Rf ./**/__pycache__; rm -Rf ./**/**/__pycache__; rm -Rf ./htmlcov; rm -Rf ./.coverage; rm -Rf ./*.xml; 

local-install: pkg-clean
	pip3 install -e .

clean-venv:
	rm -Rf .venv

setup-venv:
	python3 -m venv .venv

install-deps:
	pip3 install --upgrade pip && pip3 install -r ./environment/requirements.txt
