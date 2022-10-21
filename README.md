# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Trello

A Trello account is needed to use this program. An account can be created for free on the [Trello website](https://trello.com/). After creating an account, obtain an API key and token; storing them as `TRELLO_API_KEY` and `TRELLO_API_TOKEN` in the `.env` file respectively.

Create a board with three lists called 'To Do', 'Doing', and 'Done', and store the board ID as `TRELLO_BOARD_ID` in the `.env` file.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Docker

Build and run the app using Docker by running the following:

For dev:
```bash
docker build --target development --tag todo-app:dev .
docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev
```

For prod:
```bash
docker build --target production --tag todo-app:prod .
docker run --env-file ./.env -p 5000:5000 todo-app:prod
```
The app can now be accessed at [`http://localhost:5000/`](http://localhost:5000/)

To run tests:
```bash
docker build --target test --tag todo-app:test .
docker run todo-app:test
```

## Testing

The codebase contains unit tests and integration tests.

Run all tests with `poetry run pytest`, or run individual tests with `poetry run pytest path/to/test_file`.

## Azure

This codebase is deployed to Azure at [https://framasw-todo-app.azurewebsites.net/](https://framasw-todo-app.azurewebsites.net/).

Any updates to the main branch will update the deployed app if the build succeeds.