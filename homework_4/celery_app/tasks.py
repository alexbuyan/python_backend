import os
from typing import List

from celery import Celery

from api import pokemons as api

RMQ_URL = os.getenv("RMQ_URL", "pyamqp://user:pass@rabbitmq:5672")
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

celery_app = Celery("tasks", broker=RMQ_URL, backend=REDIS_URL)


@celery_app.task(name="pokemons.process")
def get_all_pokemons_abilities_task(pokemon_names: List[str]):
    data: dict = {}
    for pokemon_name in pokemon_names:
        data.update(api.get_pokemon_abilities(pokemon_name))
    return data
