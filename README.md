# Python Template

This is a [cookiecutter](https://github.com/audreyr/cookiecutter) template for Python projects following modern packaging conventions. Based on [Jace's Python Template](https://github.com/jacebrowning/template-python) -- thanks!

## Features

* `poetry`-based `pyproject.toml` for managing dependencies and package metadata.
* Linters: `flake8` and `mypy`.
* Code formatters: `black` and `isort`.
* `bumpver` for version tracking (either calendar or semantic versioning schemas).
* Pre-configured Azure DevOps CI pipelines.
* Tooling to launch an IPython session / Jupyter notebook with automatic reloading enabled.


## Usage

1. Install [`cookiecutter`](https://pypi.org/project/cookiecutter/) (recommended via `pipx`) and [`poetry`](https://python-poetry.org/)

```
pipx install cookiecutter
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

2. generate a project:
The eon-seed needs to be repalced by your azure devops token. 

```
cookiecutter https://eon-seed@dev.azure.com/eon-seed/Central%20Risk/_git/python-project-template -f
```

Cookiecutter will ask you for some basic info (your name, project name, project type,  etc.) and generate a base Python project for you.


## Using poetry

`cd` into the project directory first:

Create a virtual environment and install all dependencies:
```
poetry install
```

If you select `use_international_collaboration_packages = 'y'` then environment variable `POETRY_HTTP_BASIC_AZURE_PASSWORD` (Azure DevOps auth. token with right for `packaging read`)
needs to be accessible.

Hence in pipeline settings we need to create following variables:
    - PoetryHTTPBasicPassword (will be used as POETRY_HTTP_BASIC_AZURE_PASSWORD)
## Publish to Azure Artifacts

If you select `project type = 'python_package'` and `auto publish = 'y'` then the CI pipeline is pre-configured to build and publish the result of `poetry build` to `Azure Artifacts` (https://eon-seed.visualstudio.com/Data%20Platform/_packaging?_a=feed&feed=portfolio-strategy-python).

Following environment variables need to be accessible:
    - PoetryPypiTokenEMDP (will be used as POETRY_PYPI_TOKEN_EMDP)
    - PoetryRepositoriesEMDPURL (will be used as POETRY_REPOSITORIES_EMDP_URL)

## Publish docker container to Container Registry

For dockerize applications (e.g. `project type = 'fast_api'`) with `auto publish = 'y'` the CI pipeline is pre-configured to build docker container at selected empowered environment container registry and to publish it to selected container registry (*datemenctre* - https://portal.azure.com/#@ADEEQP.onmicrosoft.com/resource/subscriptions/da80dbc4-7dd6-4833-b66e-f6dbbbe42ece/resourceGroups/dat-emen-cr-rg/providers/Microsoft.ContainerRegistry/registries/datemenctre/overview, *datemenpsctre* - https://portal.azure.com/#@ADEEQP.onmicrosoft.com/resource/subscriptions/da80dbc4-7dd6-4833-b66e-f6dbbbe42ece/resourceGroups/dat-emen-ps-rg/providers/Microsoft.ContainerRegistry/registries/datemenpsctre/overview). 


If you select `use_international_collaboration_packages = 'y'` then environment variable `POETRY_HTTP_BASIC_AZURE_PASSWORD` (Azure DevOps auth. token with right for `packaging read`)
needs to be accessible.

Hence in build pipeline settings we need to create following variables:
    - PoetryHTTPBasicPassword (will be used as POETRY_HTTP_BASIC_AZURE_PASSWORD)