#!/usr/bin/env python3

import os
import logging
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from {{cookiecutter.project_slug}}.factory import create_app

app = create_app()

if os.getenv('ENV_TYPE') == 'dev':
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
elif os.getenv('ENV_TYPE') == 'prod':
    sentry_dsn = os.getenv('SENTRY_DSN')

    if sentry_dsn:
        sentry_sdk.init(sentry_dsn, integrations=[FlaskIntegration()])


if __name__ == '__main__':
    app.run()
