### Установка зависимостей

Локально создаем и запускаем виртуальное окружение

```
conda create -n venv python=3.10
conda activate venv
```

Устанавливай Poetry и зависимости

```
pip install poetry
poetry install
```

Проверяем наличие `uvicorn` командой `uvicorn --help`

Запускаем приложение командой `uvicorn app.main:app --reload`
