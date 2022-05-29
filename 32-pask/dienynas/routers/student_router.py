from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload
import models
import schemas
from database import get_db
from typing import List

router = APIRouter(
    prefix='/api/task',
    tags=['Student']
)


@router.get('/students', response_name=List[schemas.StudentAll])
def all_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


@router.post('/create')
def student_create(request: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(
        first_name=request.first_name,
        last_name=request.last_name,
        Year=request.Year,
        year_study=request.year_study,

        lit_avg=request.lit_avg,
        math_avg=request.math_avg,
        it_avg=request.it_avg,
        eng_avg=request.eng_avg,
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student
