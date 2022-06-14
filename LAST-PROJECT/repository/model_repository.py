from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def check(object, id):
    if not object.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Model with id {id} not found"
        )


def create(request: schemas.CarBrandCreate, brand_id: int, db: Session):
    new_model = models.Model(
        model=request.model,
        brand_id=brand_id
    )
    db.add(new_model)
    db.commit()
    db.refresh(new_model)

    return new_model


def get_all(db: Session):
    return db.query(models.Model).all()


def update(id: int, request: schemas.ModelCreate, db: Session):
    model = db.query(models.Model).filter(models.Model.id == id)

    check(model, id)

    model.update(request.dict())
    db.commit()

    return model.first()


def delete(id: int, db: Session):
    model = db.query(models.Model).filter(models.Model.id == id)

    check(model, id)

    model.delete()
    db.commit()

    return {"details": "Success"}
