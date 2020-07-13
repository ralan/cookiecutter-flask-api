import os
import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from celery import Celery

if os.getenv("ENV_TYPE") == "prod":
    sentry_dsn = os.getenv("SENTRY_DSN")

    if sentry_dsn:
        sentry_sdk.init(sentry_dsn, integrations=[CeleryIntegration()])

if os.getenv("BROKER_URL"):
    broker_url = os.getenv("BROKER_URL")
else:
    broker_host = os.getenv("BROKER_HOST", "{{cookiecutter.project_slug}}_broker")
    broker_url = f"pyamqp://guest@{broker_host}//"

celery = Celery("{{cookiecutter.project_slug}}", broker=broker_url)


@celery.task(ignore_result=True)
def hello():
    print("hello world")
