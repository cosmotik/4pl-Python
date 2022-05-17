from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas

router = APIRouter(
    prefix='/api/users',
    tags=["Users"]
)


@router.get('', response_model=List[schemas.HumanShortGetInfoSchema])
def all(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.post('')
def create(request: schemas.UserPostSchema, db: Session = Depends(get_db)):
    new_user = models.User(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
