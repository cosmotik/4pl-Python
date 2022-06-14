from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DATE, Float
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    setting_id = Column(Integer, ForeignKey("settings.id"))
    settings = relationship("UserSettings", back_populates='user')


class UserSettings(Base):
    __tablename__ = "Settings"

    id = Column(Integer, primary_key=True, index=True)
    consumption = Column(Float)
    odometer = Column(Float)
    user = relationship('User', back_populates='settings', uselist=False)


class CarBrand(Base):
    __tablename__ = "Carbrands"
    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String)

    models = relationship("Model", back_populates='brand')
    car = relationship("Car", back_populates="brand")


class CarModel(Base):
    __tablename__ = "CarModels"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    brand = relationship("CarBrand", back_populates="models")
    car = relationship("Car", back_populates="model")


class Mileage_record(Base):
    id = Column(Integer, primary_key=True, index=True)
    record = Column(Float)
    Created = Column(Float)
    car = relationship("Car", back_populates="record")


class Car(Base):
    __tablename__ = "cars"

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("CarBrand", back_populates="car")

    brand_id = Column(Integer, ForeignKey("brands.id"))
    brand = relationship("CarBrand", back_populates="car")

    model_id = Column(Integer, ForeignKey("models.id"))
    model = relationship("Model", back_populates="car")

    record_id = Column(Integer, ForeignKey("records.id"))
    record = relationship("Mileage_record", back_populates="car")
