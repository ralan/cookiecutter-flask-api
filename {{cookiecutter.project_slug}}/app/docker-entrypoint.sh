#!/bin/bash 

while ! mysqladmin ping -h ${DB_HOST:-{{cookiecutter.project_slug}}_db} --silent; do
    echo "Waiting for database connection"
    sleep 1
done

case $1 in
tests)
    echo "Running tests"
    exec pytest tests/${@:2}
    ;;
*)
    flask db upgrade head

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
