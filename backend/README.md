# Instructions for running backend part of the vacancies searching site

## Getting started

```shell
$ cd backend
```

Create and activate virtual environment, then install the dependencies from `requirements.txt` using the command:
```shell
$ pip install -r requirements.txt
```

## How to run the server

To run the server, use the following command:

```shell
$ uvicorn app.main:app --host localhost --port 8000 --reload
```

This will spin up the server at `http://localhost:8000` with the postgres database:

```
SQLALCHEMY_DATABASE_URL = "postgresql://team:password@68.183.220.246/jobs"
```

Or you can use local database for testing purposes instead. To do so you need to uncomment these lines in database.py:

```
import os

CUR_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(CUR_DIR, 'jobs.db')

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"
```

## How To Run the Unit Tests
To run the Unit Tests use:
```shell
$ pytest 
```

This will spin up a test database in SQLite `test_db.db`, run the tests and then tear down the database. 

You can use `pytest -v` for verbose output and `pytest -s` to disable output capture for better debugging.

To run tests with local postgres db you can use flag `--dburl`

```shell
$ pytest --dburl=postgresql://myuser:mypassword@localhost:5433/mydatabase_test
```