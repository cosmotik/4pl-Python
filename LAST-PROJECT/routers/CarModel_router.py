from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload
import models
import schemas
from database import get_db
from typing import List

router = APIRouter(
    prefix='/api/Users',
    tags=['Models']
)


@router.get('/models', response_model=List[schemas.CarModelAll])
def all_models(db: Session = Depends(get_db)):
    return db.query(models.CarModel).all()


@router.post('/create_model')
def model_create(request: schemas.CreateCarModel, db: Session = Depends(get_db)):
    new_model = models.CarModel(
        title_module=request.title_module,
    )
    db.add(new_model)
    db.commit()
    db.refresh(new_model)

    return new_model
