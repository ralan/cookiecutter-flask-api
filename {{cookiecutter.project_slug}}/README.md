# {{cookiecutter.project_name}} API

{{cookiecutter.project_short_description}}


### Prerequisites

The easiest way to run this app is by using `Docker` and `Docker Compose.`

To install Docker and Docker Compose, follow instructions at https://docs.docker.com/engine/install/
and https://docs.docker.com/compose/install/.


### Installing the {{cookiecutter.project_name}} app

1. Clone the repo

2. Copy `dotenv` file to `.env` and set values

3. Build the app

```
$ docker-compose build
```


### Run the app in production mode

```
$ docker-compose up
```

The app should be available at http://localhost/ui.


### Run the app in development mode

```
docker-compose -f docker-compose.dev.yml up
```

The app should be available at http://localhost:8080/ui.


### Run tests

```
docker-compose -f docker-compose.test.yml up --abort-on-container-exit
```


### Security

It is highly recommended to create and use a regular database user, but not `root`.
Furthermore, consider using a secrets manager, e.g., Vault by HashiCorp.

