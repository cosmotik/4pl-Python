from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/Brands',
    tags=['Brands']
)


@router.get('')
def all_brands(active: int, db: Session = Depends(get_db)):
    if active < 0 or active > 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wrong active state passed"
        )
    return db.query(models.Post) \
        .join(models.PostSettings) \
        .options(selectinload(models.Post.owner)) \
        .options(selectinload(models.Post.settings)) \
        .filter(models.PostSettings.is_active == active).all()


@router.post('/create_brand')
def create_brand(request: schemas.CreateCarBrand, db: Session = Depends(get_db)):
    new_brand = models.CarBrand(
        title_brand=request.title_brand,
    )

    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand
