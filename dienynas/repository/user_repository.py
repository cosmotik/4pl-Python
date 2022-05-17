from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def analize(user, id):
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )

def get_all_users(db: Session):
    return db.query(models.User).all()


def get_single_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    analize(user, id)

    return user.first()


def update(id: int, request: schemas.UserPostSchema, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    analize(user, id)

    user.update(request.dict())
    db.commit()

    return user.first()


def delete(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    analize(user, id)

    user.delete()
    db.commit()

    return {"details": "Success"}


def create(request: schemas.UserPostSchema, db: Session):
    new_user = models.User(
        first_name=request.first_name,
        last_name=request.last_name,
        It_avg_grade=request.It_avg_grade,
        Eng_avg_grade=request.Eng_avg_grade,
        Math_avg_grade=request.Math_avg_grade
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
