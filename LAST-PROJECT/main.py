from fastapi import FastAPI
from database import engine
from routers import user_router
import models

app = FastAPI()

app.include_router(user_router.router)
models.Base.metadata.create_all(engine)