import uvicorn
from fastapi import FastAPI

from routers.pokemons import router

app = FastAPI()
app.include_router(router=router)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 80
    uvicorn.run(app, host=host, port=port)
