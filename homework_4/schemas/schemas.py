from typing import List

from pydantic import BaseModel


class Pokemons(BaseModel):
    pokemon_names: List[str]
