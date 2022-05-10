from fastapi import FastAPI
from routers import main_urls

app = FastAPI()
app.include_router(main_urls.router)