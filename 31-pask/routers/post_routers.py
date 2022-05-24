from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/post',
    tags=['Posts']
)

@router.get('')
def all(active: int, db: Session = Depends(get_db)):
    if active < 0 or active > 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wrong active state passed"
        )
    return db.query(models.Post)\
            .join(models.PostSettings)\
            .options(selectinload(models.Post.owner))\
            .options(selectinload(models.Post.settings))\
            .filter(models.PostSettings.is_active == active).all()

@router.post('/create/{user_id}')
def create_post(request: schemas.BlogCreate, user_id: int, db: Session = Depends(get_db)):
    new_settings = models.PostSettings(
        is_active=request.settings.is_active
    )

    db.add(new_settings)
    db.commit()
    db.refresh(new_settings)

    new_post = models.Post(
        title=request.title,
        body=request.body,
        owner_id=user_id,
        settings_id=new_settings.id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
