from database import Base
from sqlalchemy import Column, Integer, String, Float


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    It_avg_grade = Column(Float)
    Eng_avg_grade = Column(Float)
    Math_avg_grade = Column(Float)
