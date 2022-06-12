from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DATE, Float
from sqlalchemy.orm import relationship


class CarBrand(Base):
    __tablename__ = "Car_Brand"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    models = relationship("CarModel", back_populates="brands")

class CarModel(Base):
    __tablename__ = "Car_Model"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    brands = relationship("CarBrand", back_populates='models')
    description = relationship("CarDescription", back_populates='model_description')
    record = relationship("Record", back_populates='model_record')
    brand_id = Column(Integer, ForeignKey("Car_brand.id"))


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    user = relationship("UserSettings", back_populates='setting', uselist=False)

class UserSettings(Base):
    __tablename__ = "Settings"

    id = Column(Integer, primary_key=True, index=True)
    consumption = Column(Float)
    odometer_mile = Column(Float)
    odometer_kilometer = Column(Float)
    setting = relationship('User', back_populates='user')


class CarDescription(Base):
    __tablename__ = "Discription"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    model_description = relationship('CarModel', back_populates='description')


class Record(Base):
    __tablename__ = "Car_Record"

    id = Column(Integer, primary_key=True, index=True)
    TypeOfRecord = Column(String, index=True)
    model_record = relationship("CarModel", back_populates='record')