from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def check(user, id):
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )


def create(request: schemas.UserCreate, db: Session):
    new_settings = models.UserSettings(
        Consumption=request.settings.Consumption,
        Odometer=request.settings.Odometer
    )
    db.add(new_settings)
    db.commit()
    db.refresh(new_settings)

    new_user = models.User(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        settings_id=new_settings.id,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all_users(db: Session):
    return db.query(models.User).all()


def update(id: int, request: schemas.UserUpdate, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    check(user, id)

    user.update(request.dict())
    db.commit()

    return user.first()


def delete(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    check(user, id)

    user.delete()
    db.commit()

    return {"details": "Success"}

