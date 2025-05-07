from typing import Dict
from fastapi import FastAPI

import {{cookiecutter.package_name}}


app = FastAPI()

@app.get("/")
def get_version() -> Dict[str, str]:
    return {"verison": {{cookiecutter.package_name}}.__version__}