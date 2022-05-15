from pydantic import BaseModel


class HumanShortGetInfoSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True


class UserPostSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
