from fastapi import FastAPI
from database import engine
from routers import user_router, CarBrand_router, CarModel_router, description_router, record_router, UserSettigns_router
import models

app = FastAPI()

app.include_router(user_router.router)
app.include_router(CarBrand_router.router)
app.include_router(CarModel_router.router)

models.Base.metadata.create_all(engine)
