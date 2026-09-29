from fastapi import FastAPI

from .database import Base, engine
from . import models
from .api.routes import companies, people


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Lead Generation API",
    description="API for discovering and enriching professional leads",
    version="1.0.0"
)


app.include_router(companies.router)
app.include_router(people.router)


@app.get("/")
def root():
    return {
        "message": "Lead Generation API is running!"
    }