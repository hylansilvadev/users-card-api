from typing import List, Optional

from firedantic import Model
from pydantic import BaseModel


class UserCreate(BaseModel):
    imageUrl: Optional[str] = None
    name: str
    tags: List[str] = []
    linkedin: Optional[str] = None
    instagram: Optional[str] = None
    github: Optional[str] = None


class User(Model):
    __collection__ = 'users'
    imageUrl: Optional[str] = None
    name: str
    tags: List[str] = []
    linkedin: Optional[str] = None
    instagram: Optional[str] = None
    github: Optional[str] = None
