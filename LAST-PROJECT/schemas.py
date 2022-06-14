from pydantic import BaseModel
from typing import List
from datetime import datetime


class UserSettingsCreate(BaseModel):
    Consumption: float
    Odometer: float


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    settings: UserSettingsCreate


class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str


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


class CarModelCreate(BaseModel):
    model: str


class CarModelAll(BaseModel):
    id: int
    model: str

    class Config:
        orm_mode = True


class CarBrandAll(BaseModel):
    id: int
    brand_name: str
    models: List[CarModelAll] = []

    class Config:
        orm_mode = True


class CreateCar(BaseModel):
    user: UserCreate
    brand: CarBrandCreate
    model: CarModelCreate


class CarAll(BaseModel):
    user: UserAll
    brand: CarBrandAll
    model: CarModelAll
