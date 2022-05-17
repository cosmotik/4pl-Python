from pydantic import BaseModel


class HumanShortGetInfoSchema(BaseModel):
    first_name: str
    last_name: str
    It_avg_grade: float

    class Config:
        orm_mode = True


class UserPostSchema(BaseModel):
    first_name: str
    last_name: str
    It_avg_grade: float
    Eng_avg_grade: float
    Math_avg_grade: float
