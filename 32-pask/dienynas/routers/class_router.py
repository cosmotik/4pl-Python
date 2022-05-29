from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload
import models
import schemas
from database import get_db
from typing import List

router = APIRouter(
    prefix='/api/task',
    tags=['Class']
)


@router.get('')
def all(active: int, db: Session = Depends(get_db)):
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


@router.post('/create/{user_id}')
def create_post(request: schemas.ClassCreate, boss_id: int, db: Session = Depends(get_db)):

    new_class = models.Post(
        title=request.title,
        boss_id=boss_id
    )

    db.add(new_class)
    db.commit()
    db.refresh(new_class)

    return new_class
