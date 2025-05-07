import os
import shutil
from typing import Dict, Iterable, Optional
import subprocess

DONT_AUTO_UPDATE_THESE_PACKAGES = [
    "sphinx",  # As of Jan 2023, latest sphinx is incompatible with latest sphinx-rtd-theme.
]


## Copy project-type-specific example files

if os.path.exists(
    example_files_folder := os.path.join(
        os.getcwd(), "cookiecutter_examples", "{{cookiecutter.project_type}}"
    )
):
    shutil.copytree(example_files_folder, os.getcwd(), dirs_exist_ok=True)
else:
    print("example files for {{cookiecutter.project_type}} not found")

shutil.rmtree(os.path.join(os.getcwd(), "cookiecutter_examples"))


## upgrade dev packages


def _extract_section_from_toml(
    toml_lines: Iterable[str], section_label: str
) -> Dict[str, str]:
    # apologies, here we reimplement TOML-parser. We could just "import toml", but
    # problem is that this is not included in many "default" Python installations,
    # which is usually the place from where we invoke cookiecutter.
    # With Python 3.11, we can just use Python stdlib's veresion "tomllib". But then
    # we would need to have that as minimum Python version. As of Jan-2023, that is
    # not a good idea yet.
    section_data: Dict[str, str] = dict()
    current_section_label: Optional[str] = None
    for line in toml_lines:
        stripped_line = line.strip()
        if stripped_line.startswith("#"):
            continue
        if stripped_line.startswith("[") and stripped_line.endswith("]"):
            current_section_label = stripped_line.strip("[]")
        if current_section_label == section_label:
            splitted_line = stripped_line.split("=")
            if len(splitted_line) != 2:
                continue
            key, value = splitted_line
            section_data[key.strip()] = value.strip()

    return section_data


# TODO: when udpating CR-poetry min required version to 1.2+/1.3+, remove this branching.
POETRY_DEV_SECTION_LABEL = '{% if cookiecutter.empowered_environment == "Central Risk" %}tool.poetry.dev-dependencies{%elif cookiecutter.empowered_environment == "Portfolio Strategy" %}tool.poetry.group.dev.dependencies{% endif %}'
POETRY_DEV_UPDATE_COMMAND = '{% if cookiecutter.empowered_environment == "Central Risk" %}poetry add -D{%elif cookiecutter.empowered_environment == "Portfolio Strategy" %}poetry add --group dev{% endif %}'

with open("pyproject.toml", "r") as pyproject_file:
    packages_to_upgrade = list(
        _extract_section_from_toml(
            toml_lines=pyproject_file.readlines(),
            section_label=POETRY_DEV_SECTION_LABEL,
        ).keys()
    )
update_command = POETRY_DEV_UPDATE_COMMAND.split(" ") + [
    f"{package}@latest"
    for package in packages_to_upgrade
    if package not in DONT_AUTO_UPDATE_THESE_PACKAGES
]
print(f"Updating dev dependencies:\n{' '.join(update_command)}")
subprocess.run(update_command)
