from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from repository import user_repository as repo
import models
import schemas

router = APIRouter(
    prefix='/api/users',
    tags=["Users"]
)


@router.get('', response_model=List[schemas.HumanShortGetInfoSchema])
def all(db: Session = Depends(get_db)):
    return repo.get_all_users(db)


@router.get('/{id}', response_model=schemas.HumanShortGetInfoSchema)
def get_single_by_id(id: int, db: Session = Depends(get_db)):
    return repo.get_single_by_id(id, db)


@router.put('/update/{id}')
def update(id: int, request: schemas.UserPostSchema, db: Session = Depends(get_db)):
    return repo.update(id, request, db)


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete(id, db)

@router.post('')
def create(request: schemas.UserPostSchema, db: Session = Depends(get_db)):
    return repo.create(request, db)
