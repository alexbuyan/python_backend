from celery.result import AsyncResult
from fastapi import APIRouter, Body, Path, status
from fastapi.responses import Response
from src.models.main import Servers

router = APIRouter()


@router.post("/order_servers/")
async def order_servers(servers: Servers):
    task = 


@router.post("/hell")
def router_2():
    pass
