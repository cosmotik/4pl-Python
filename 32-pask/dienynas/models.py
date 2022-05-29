from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DATE, Float
from sqlalchemy.orm import relationship
from datetime import datetime


class Class(Base):
    __tablename__ = 'class'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

    student = relationship("Student", back_populates='class_')
    boss_id = Column(Integer, ForeignKey('boss.id'))
    boss = relationship('Boss', back_populates='class_')

class Boss(Base):
    __tablename__ = 'boss'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

    student = relationship("Student", back_populates='boss')
    class_ = relationship("Class", back_populates='boss', uselist=False)


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    Year = Column(datetime)
    year_study = Column(datetime)

    lit_avg = Column(Float)
    math_avg = Column(Float)
    it_avg = Column(Float)
    eng_avg = Column(Float)

    boss_id = Column(Integer, ForeignKey("boss.id"))
    boss = relationship('Boss', back_populates='student')

    class_id = Column(Integer, ForeignKey("class_id"))
    class_ = relationship('Class', back_populates='student')
