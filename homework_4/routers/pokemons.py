from fastapi import APIRouter

from celery_app.tasks import celery_app
from celery_app.utils import get_task_info
from schemas.schemas import Pokemons

router = APIRouter()


@router.post("/")
def root() -> dict:
    return {"Info": "Please visit /docs for testing"}


@router.post("/pokemons")
def get_abilities(pokemons: Pokemons) -> dict:
    """
    Return the List of abilities for the pokemons provided in input in a sync way
    """
    task = celery_app.send_task(
        name="pokemons.process", kwargs={"pokemon_names": pokemons.pokemon_names}
    )
    task_id = task.id

    return {"message": "Запрос успешно отправлен", "task_id": task_id}


@router.get("/task/{task_id}")
async def get_task_status(task_id: str) -> dict:
    """
    Return the status of the submitted Task
    """
    return get_task_info(task_id)
