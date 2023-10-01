from fastapi import FastAPI
from app.routers import router

app = FastAPI(
    title="HW1 FastAPI app",
    description="HW1 FastAPI app",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)
