from fastapi import FastAPI
from database import engine
from routers import user_routers
from routers import carBrand_routers
from routers import model_routers
from routers import car_routers

import models

app = FastAPI()
app.include_router(user_routers.router)
app.include_router(carBrand_routers.router)
app.include_router(model_routers.router)

app.include_router(car_routers.router)

models.Base.metadata.create_all(engine)
