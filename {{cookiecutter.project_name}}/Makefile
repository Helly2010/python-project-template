.PHONY: all lint type test test-cov

CMD:=poetry run
PYMODULE:={{cookiecutter.package_name}}
TESTS:=tests

poetry_install:
	poetry install

all: lint type test 

lint:
	$(CMD) flake8 $(PYMODULE) $(TESTS) {% if cookiecutter.project_type=='fast_api' %} main.py  {% endif %}

type:
	$(CMD) mypy $(PYMODULE)  {% if cookiecutter.use_mypy_tests == '1' -%} $(TESTS)  {% endif %} {% if cookiecutter.project_type=='fast_api' %} main.py  {% endif %}

test:
	$(CMD) pytest --cov=$(PYMODULE) $(TESTS)

test-cov:
	$(CMD) pytest --cov=$(PYMODULE) $(TESTS) --cov-report html

isort:
	$(CMD) isort $(PYMODULE) $(TESTS)
