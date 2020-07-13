#!/bin/bash 

while ! mysqladmin ping -h ${DB_HOST:-{{cookiecutter.project_slug}}_db} --silent; do
    echo "Waiting for database connection"
    sleep 1
done

{%- if cookiecutter.add_celery == "yes" %}
while ! curl -s -u guest:guest ${BROKER_HOST:-{{cookiecutter.project_slug}}_broker_dev}:15672/api/healthchecks/node | grep "ok"; do
    echo "Waiting for message broker connection"
    sleep 1
done
{%- endif %}

case $1 in
{%- if cookiecutter.add_celery == "yes" %}
workers)
    flask db upgrade head

    if [ "$ENV_TYPE" = "dev" ];
    then
        echo "Starting Celery workers with autoreload"
        exec watchmedo auto-restart --recursive -d {{cookiecutter.project_slug}} -p '*.py' -- celery worker --uid=nobody --loglevel=debug --concurrency=2 -A {{cookiecutter.project_slug}}.tasks ${@:2}
    else
        echo "Starting Celery workers"
        exec celery worker --uid nobody --loglevel=info --concurrency=2 -A {{cookiecutter.project_slug}}.tasks ${@:2}
    fi
    ;;
{%- endif %}
tests)
    echo "Running tests"
    exec pytest tests/${@:2}
    ;;
*)
    flask db upgrade head

    {%- if cookiecutter.add_celery == "yes" %}
    while ! celery inspect ping --quiet -A {{cookiecutter.project_slug}}.tasks | grep "pong"; do
        echo "Waiting for Celery workers"
        sleep 1
    done
    {%- endif %}

    if [ "$ENV_TYPE" = "dev" ];
    then
        echo "Starting application using Flask server (development environment)"
        export FLASK_ENV=development
        export FLASK_RUN_EXTRA_FILES={{cookiecutter.project_slug}}/api/api.yaml
        exec flask run --host=0.0.0.0 --port=80 ${@:2}
    else
        echo "Starting application using Gunicorn server (production environment)"
        exec gunicorn --bind 0.0.0.0:80 --workers=2 ${@:2} app:app
    fi
    ;;
esac
