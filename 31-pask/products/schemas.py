from typing import List
from pydantic import BaseModel


class UserCreate(BaseModel):
    product: str


class BlogSettingsCreate(BaseModel):
    is_active: bool


class BlogCreate(BaseModel):
    title: str
    description: str
    settings: BlogSettingsCreate


class BlogAll(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


class UserAll(BaseModel):
    id: int
    product: str
    posts: List[BlogAll] = []

    class Config:
        orm_mode = True
