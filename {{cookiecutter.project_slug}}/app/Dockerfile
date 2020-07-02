FROM python:3.8

RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y
RUN apt-get install -y default-mysql-client

COPY requirements.txt /tmp/
RUN pip install -Ur /tmp/requirements.txt && rm /tmp/requirements.txt

COPY . /opt/app
WORKDIR /opt/app

ENV ENV_TYPE prod
EXPOSE 80

ENTRYPOINT ["./docker-entrypoint.sh"]