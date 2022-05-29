from fastapi import FastAPI
from database import engine
from routers import class_router, student_router
import models


app = FastAPI()
app.include_router(class_router.router)
app.include_router(student_router.router)

models.Base.metadata.create_all(engine)