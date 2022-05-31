from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/Users',
    tags=['Brands']
)


@router.get('', response_model=List[schemas.CarBrandAll])
def all(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.post('/create')
def create_brand(request: schemas.CreateCarBrand, db: Session = Depends(get_db)):
    new_brand = models.User(
        title=request.title
    )

    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand
