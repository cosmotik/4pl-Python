from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def check(object, id):
    if not object.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Brand with id {id} not found"
        )


def create(request: schemas.CarBrandCreate, db: Session):
    new_brand = models.CarBrand(
        brand_name=request.brand_name,
    )
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand


def get_all(db: Session):
    return db.query(models.CarBrand).all()


def update(id: int, request: schemas.CarBrandCreate, db: Session):
    brand = db.query(models.CarBrand).filter(models.CarBrand.id == id)

    check(brand, id)

    brand.update(request.dict())
    db.commit()

    return brand.first()


def delete(id: int, db: Session):
    brand = db.query(models.CarBrand).filter(models.CarBrand.id == id)

    check(brand, id)

    brand.delete()
    db.commit()

    return {"details": "Success"}
