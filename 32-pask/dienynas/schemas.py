from typing import List
from pydantic import BaseModel
from datetime import datetime


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    Year: datetime
    year_study: datetime

    lit_avg: float
    math_avg: float
    it_avg: float
    eng_avg: float


class BossCreate(BaseModel):
    first_name: str
    last_name: str


class StudentAll(BaseModel):
    id: int
    first_name: str
    last_name: str
    Year: datetime
    year_study: datetime

    class Config:
        orm_mode = True


class ClassCreate(BaseModel):
    title: str


class BossAll(BaseModel):
    id: int
    first_name: str
    last_name: str
    students: List[StudentAll]

    class Config:
        orm_mode = True
