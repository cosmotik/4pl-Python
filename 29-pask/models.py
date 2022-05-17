from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
