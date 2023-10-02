# Подготовка к работе

```
conda create -n hw2-tests-env
conda activate hw2-tests-env
cd homework_2
pip install poetry
poetry install
```

# Бизнес-сценарий

База данных Родители-Дети

В `contractors.py` описаны сущности и небольшая дополнительная бизнес логика

Само приложение находится в `main.py` и `routers.py`

# Тесты

Модульные тесты находятся в файле `test_modular.py`

Интеграционные тесты находятся в файле `test_integration.py`

Тесты запускаются при помощи команды `pytest`
