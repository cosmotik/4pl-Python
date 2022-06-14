from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def check(user, id):
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {id} not found"
        )


def create(db: Session, user_id: int, brand_id: int, model_id: int, record_id: int,):

    new_car = models.User(
        user_id=user_id,
        brand_id=brand_id,
        model_id=model_id,
        record_id=record_id,
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car


def get_all(db: Session):
    return db.query(models.Car).all()


def update(id: int, request: schemas., db: Session):
    car = db.query(models.Car).filter(models.Car.id == id)

    check(car, id)

    car.update(request.dict())
    db.commit()

    return car.first()


def delete(id: int, db: Session):
    car = db.query(models.Car).filter(models.Car.id == id)

    check(car, id)

    car.delete()
    db.commit()

    return {"details": "Success"}

