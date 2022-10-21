FROM python:3.10.5-buster as base
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "$PATH:/root/.local/bin/"
EXPOSE 5000
RUN mkdir /app
WORKDIR /app
COPY poetry.lock poetry.toml pyproject.toml ./
COPY ./todo_app ./todo_app

FROM base as production
RUN poetry install
CMD poetry run gunicorn "todo_app.app:create_app()" -- bind 0.0.0.0:${PORT:-5000}

FROM base as development
RUN poetry install --no-dev
ENTRYPOINT ["poetry", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]

FROM base as test
COPY .env.test ./
RUN poetry install --no-dev
ENTRYPOINT [ "poetry", "run", "pytest" ]
