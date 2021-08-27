from pydantic import BaseModel
from typing import List, Optional, Set
from enum import Enum


class Profession(str, Enum):
    backend_engineer = 'backend_engineer'
    frontend_engineer = 'frontend_engineer'
    data_engineer = 'data_engineer'
    full_stack_engineer = 'full_stack_engineer'


class SkillSet(BaseModel):
    name: str
    skills: Set[str]


class User(BaseModel):
    name: str
    age: Optional[int] = None
    city: str = 'srinagar'
    profession: Profession
    skill_sets: Optional[List[SkillSet]] = None
