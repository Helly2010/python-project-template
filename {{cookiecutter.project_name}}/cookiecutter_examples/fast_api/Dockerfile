FROM python:3.8 as intermediate

{% if cookiecutter.use_international_collaboration_packages != 'n' -%}
ARG POETRY_HTTP_BASIC_AZURE_PASSWORD
{% endif -%}

WORKDIR /app

RUN python -m pip install poetry

COPY pyproject.toml poetry.lock README.md main.py ./

COPY ./{{cookiecutter.package_name}} ./{{cookiecutter.package_name}}

RUN poetry install --no-dev

FROM intermediate

EXPOSE 80
CMD ["poetry" , "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]