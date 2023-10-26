FROM python:3.10

RUN pip install poetry

COPY . .

RUN poetry install

ENTRYPOINT poetry run celery -A celery_app.tasks worker --loglevel=info