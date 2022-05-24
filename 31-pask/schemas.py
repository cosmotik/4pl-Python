from typing import List
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str


class BlogSettingsCreate(BaseModel):
    is_active: bool


class BlogCreate(BaseModel):
    title: str
    body: str
    settings: BlogSettingsCreate


class BlogAll(BaseModel):
    id: int
    title: str
    body: str

    class Config:
        orm_mode = True


class UserAll(BaseModel):
    id: int
    email: str
    posts: List[BlogAll] = []

    class Config:
        orm_mode = True
