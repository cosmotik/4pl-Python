from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DATE, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    settings_id = Column(Integer, ForeignKey('settings.id'))
    settings = relationship('UserSettings', back_populates='owner')
    car = relationship('Car', back_populates='user', uselist=False)


class UserSettings(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    Consumption = Column(Float)
    Odometer = Column(Float)
    owner = relationship('User', back_populates='settings', uselist=False)


class CarBrand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String)
    models = relationship('CarModel', back_populates='brand')
    car = relationship('Car', back_populates='brand', uselist=False)


class CarModel(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    brand = relationship("CarBrand", back_populates="models")
    car = relationship('Car', back_populates='model', uselist=False)


class Car(Base):
    __tablename__ = "cars"

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="car")
    brand_id = Column(Integer, ForeignKey("brands.id"))
    brand = relationship("CarBrand", back_populates="car")
    model_id = Column(Integer, ForeignKey('models.id'))
    model = relationship('CarModel', back_populates='car')


