from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
from repository import user_repository as repo

router = APIRouter(
    prefix='/api/user',
    tags=['Users']
)


@router.post('/Create')
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return repo.create(request, db)


@router.get('/Get', response_model=List[schemas.CarAll])
def all(db: Session = Depends(get_db)):
    return repo.get_all(db)


@router.put('/Update/{id}')
def update(id: int, request: schemas.CarCreate, db: Session = Depends(get_db)):
    return repo.update(id, request, db)


@router.delete('/Delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete(id, db)
