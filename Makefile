help:
	@echo "Usage:"
	@echo "    make help        show this message"
	@echo "    make setup       create virtual environment and install dependencies"
	@echo "    make activate    enter virtual environment"
	@echo "    make test        run the test suite"
	@echo "    exit             leave virtual environment"

setup:
	pip install pipenv
	pipenv install --dev --three

activate:
	pipenv shell -c

test:
	pipenv run -- py.test tests -s -v

tox-test:
	tox -e $(echo py$TRAVIS_PYTHON_VERSION | tr -d .)

.PHONY: help activate test tox-test

