from app.routers import router
from fastapi import FastAPI

app = FastAPI(
    title="HW2 Tests",
    description="HW2 Tests",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)
