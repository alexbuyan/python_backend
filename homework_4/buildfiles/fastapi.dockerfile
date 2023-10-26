FROM python:3.10

RUN pip install poetry

COPY . .

RUN poetry install

EXPOSE 80
CMD ["poetry", "run", "python", "main.py"]