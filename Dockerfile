FROM python:3.10.5-buster as base
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "$PATH:/root/.local/bin/"
EXPOSE 5000
RUN mkdir /app
WORKDIR /app
COPY poetry.lock poetry.toml pyproject.toml .env.test ./
COPY ./todo_app ./todo_app

FROM base as production
RUN poetry install
ENTRYPOINT ["poetry", "run", "gunicorn",  "-b", "0.0.0.0:5000", "todo_app.app:create_app()"]

FROM base as development
RUN poetry install --no-dev
ENTRYPOINT ["poetry", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]

FROM base as test
RUN poetry install --no-dev
ENTRYPOINT [ "poetry", "run", "pytest" ]
