import os

from pydantic_settings import BaseSettings


class Configuration(BaseSettings):
    broker: str = os.getenv("BROKER")
    backend: str = os.getenv("BACKEND")


config = Configuration()
