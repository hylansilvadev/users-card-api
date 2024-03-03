from typing import List

from pydantic import BaseModel


class Member(BaseModel):
    name: str
    tags: List[str] = ["Membro"]
    instagram: str
    linkedin: str
    github: str
