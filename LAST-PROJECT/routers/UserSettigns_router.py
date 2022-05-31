from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/Users',
    tags=['UserSettings']
)
