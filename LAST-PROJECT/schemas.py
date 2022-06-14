from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserSettingsCreate(BaseModel):
    Consumption: float
    Odometer: float


class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    settings: UserSettingsCreate


class SettingsAll(BaseModel):
    id: int
    Consumption: float
    Odometer: float

    class Config:
        orm_mode = True


class UserAll(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    settings: SettingsAll

    class Config:
        orm_mode = True


class CarBrandCreate(BaseModel):
    brand_name: str


class ModelCreate(BaseModel):
    model: str


class ModelAll(BaseModel):
    id: int
    model: str

    class Config:
        orm_mode = True


class CarBrandAll(BaseModel):
    id: int
    brand_name: str
    models: List[ModelAll] = []

    class Config:
        orm_mode = True


class CreateCar(BaseModel):
    pass


class CarAll(BaseModel):
    user: UserAll
    brand: CarBrandAll
    model: ModelAll
