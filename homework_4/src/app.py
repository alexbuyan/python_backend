from fastapi import FastAPI
from homework_4.src.router.main import router

app = FastAPI()

app.include_router(router=router)
