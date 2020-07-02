FROM mysql:8.0

RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y

COPY custom.cnf /etc/mysql/conf.d/custom.cnf

ENV MYSQL_DATABASE {{cookiecutter.project_slug}}