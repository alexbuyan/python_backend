import json

from celery.result import AsyncResult


def get_task_info(task_id: str) -> dict:
    task = AsyncResult(task_id)

    if task.state == "SUCCESS":
        response = {"status": task.state, "result": task.get()}
    elif task.state == "FAILURE":
        response = json.loads(
            task.backend.get(task.backend.get_key_for_task(task.id)).decode("utf-8")
        )
        del response["children"]
        del response["traceback"]
    else:
        response = {"status": task.state, "result": task.info}

    return response
