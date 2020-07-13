import os
import shutil

if "{{ cookiecutter.add_celery }}" == "no":
    os.remove("app/{{cookiecutter.project_slug}}/tasks.py")
    shutil.rmtree("broker")