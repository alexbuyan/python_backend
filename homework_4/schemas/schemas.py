from typing import List, Optional

from pydantic import BaseModel


class Country(BaseModel):
    country_name: str


class Domain(BaseModel):
    domain_name: str
    country: Optional[Country]


class Hosting(BaseModel):
    hosting_name: str
    domains: List[Domain]
