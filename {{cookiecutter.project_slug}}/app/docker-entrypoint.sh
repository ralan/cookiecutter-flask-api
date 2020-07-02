#!/bin/bash 

while ! mysqladmin ping -h ${DB_HOST:-{{cookiecutter.project_slug}}_db} --silent; do
    echo "Waiting for database connection"
    sleep 1
done

case $ENV_TYPE in
prod)
    echo "Starting application using Gunicorn server (production environment)"
    flask db upgrade head
    exec gunicorn --bind 0.0.0.0:80 --workers=2 ${@:2} app:app
    ;;
dev)
    echo "Starting application using Flask server (development environment)"
    flask db upgrade head
    export FLASK_ENV=development
    export FLASK_RUN_EXTRA_FILES={{cookiecutter.project_slug}}/api/api.yaml
    exec flask run --host=0.0.0.0 --port=80 ${@:2}
    ;;
test)
    echo "Running tests"
    exec pytest tests/${SELECTED_TESTS}
    ;;
*)
    echo "Set ENV_TYPE to 'prod', 'dev' or 'test'"
    ;;
esac
