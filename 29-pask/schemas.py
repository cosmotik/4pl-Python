from pydantic import BaseModel


class HumanShortGetInfoSchema(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserPostSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
