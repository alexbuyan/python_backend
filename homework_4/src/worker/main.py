from celery import Celery
from src.config import config

celery = Celery("server_hosting", broker=config.broker, backend=config.backend)


@celery.task
def task() -> bytes:
    pass
