from typing import List

from pydantic import BaseModel, RootModel


class Server(BaseModel):
    server_id: int
    configuration: str
    price_per_hour: int


class Servers(RootModel):
    servers: List[Server]
