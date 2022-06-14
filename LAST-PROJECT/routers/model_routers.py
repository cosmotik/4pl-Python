from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
from repository import model_repository as repo

router = APIRouter(
    prefix='/api/model',
    tags=['Models']
)


@router.post('/create/{CATEGORY_id}')
def create_model(request: schemas.ModelCreate, brand_id: int, db: Session = Depends(get_db)):
    return repo.create(request, brand_id, db)


@router.get('/Get', response_model=List[schemas.ModelAll])
def all(db: Session = Depends(get_db)):
    return repo.get_all(db)


@router.put('/Update/{id}')
def update(id: int, request: schemas.ModelCreate, db: Session = Depends(get_db)):
    return repo.update(id, request, db)


@router.delete('/Delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete(id, db)
