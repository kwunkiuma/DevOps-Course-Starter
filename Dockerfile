FROM python:3.10.5-buster as base
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "$PATH:/root/.local/bin/"
EXPOSE 5000
RUN mkdir /app
WORKDIR /app
COPY poetry.lock poetry.toml pyproject.toml ./
RUN poetry install
COPY ./todo_app ./todo_app

FROM base as production
ENTRYPOINT ["poetry", "run", "gunicorn",  "-b", "0.0.0.0:5000", "todo_app.app:create_app()"]

FROM base as development
ENTRYPOINT ["poetry", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]
