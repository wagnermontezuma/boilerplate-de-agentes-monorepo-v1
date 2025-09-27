# base image
FROM python:3.11-slim as base

# install poetry
RUN pip install poetry

# set up poetry
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --without dev --no-interaction --no-ansi --no-root

# copy application code
COPY . .

# run the application
CMD ["poetry", "run", "litestar", "--app-dir", "apps/backend", "run"]
