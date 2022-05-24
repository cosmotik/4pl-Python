from fastapi import FastAPI
from database import engine
from routers import user_routers, post_routers
import models


app = FastAPI()
app.include_router(user_routers.router)
app.include_router(post_routers.router)

models.Base.metadata.create_all(engine)