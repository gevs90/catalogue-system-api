# Test catalogue-micro-fastApi

In this repository, the test was developed to propose a microservice structure, proposed to resolve the demand for services with a view to a production environment and be scalable in the future, offering standards for APIs, documentation and using Postgres as a database.

## How to install

Clone this repository

```bash
$ git clone git@github.com:gevs90/catalogue-system-api.git
```

```bash
$ cd catalogue-system-api
```

## How to run locally on your computer

Configure the DSN string to your Postgres database in `.env` file, 
or provide it from the environment variable `DSN_DATABASE`.

To run the application use following.

```bash
$ python3 -m venv venv
```

Use venv to make a cumstom commando for create user admin.
```bash
$ source venv/bin/activate
```

Install using python version 3.11.
```bash
$ pip install --editable .
```


Create user admin system.
```bash
$ create_user admin --name 'Administrator' --email admin@admin.text --password admin1234
```
Run app
```bash
$ uvicorn app.main:app
```
or 
```bash
$ DSN_DATABASE=postgresql://... uvicorn app.main:app
```
## How to run with docker

```bash
$ docker-compose up -d
```

## License

MIT License (see [LICENSE](https://opensource.org/license/unlicense)).