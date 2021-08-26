from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    city: str
    married: bool
