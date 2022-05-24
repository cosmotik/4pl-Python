from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/Users',
    tags=['Users']
)


@router.get('', response_model=List[schemas.UserAll])
def all(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.post('/create')
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(
        email=request.email,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
