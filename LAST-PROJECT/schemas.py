from typing import List
from pydantic import BaseModel


class CreateCarBrand(BaseModel):
    title: str


class CarBrandAll(BaseModel):
    title: str

    class Config:
        orm_mode = True


class CreateCarModel(BaseModel):
    title: str


class CarModelAll(BaseModel):
    title: str

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserAll(BaseModel):
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


class UserSettings(BaseModel):
    consumption: float
    odometer_mile: float
    odometer_kilometer: float


class Descriptions(BaseModel):
    description: str


class Records(BaseModel):
    record: str
