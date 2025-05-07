FROM python:3.9 as intermediate

{% if cookiecutter.use_international_collaboration_packages != 'n' -%}
ARG POETRY_HTTP_BASIC_AZURE_PASSWORD
{% endif -%}
WORKDIR /job

RUN python -m pip install poetry

COPY pyproject.toml poetry.lock README.md ./

COPY ./{{cookiecutter.package_name}} ./{{cookiecutter.package_name}}

RUN poetry install --no-dev

FROM intermediate

CMD poetry run python {{cookiecutter.package_name}}/run.py --arg_1 $arg_1 --arg_2 $arg_2