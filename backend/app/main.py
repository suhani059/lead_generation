from fastapi import FastAPI

from .database import Base, engine
from . import models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Lead Generation API",
    description="API for discovering and enriching professional leads",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Lead Generation API is running!"
    }

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    normalized_name = Column(String, nullable=False)

    domain = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)

    industry = Column(String, nullable=True)
    country = Column(String, nullable=True)

    people = relationship(
        "Person",
        back_populates="company"
    )


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)
    normalized_name = Column(String, nullable=False)

    job_title = Column(String, nullable=True)
    normalized_job_title = Column(String, nullable=True)

    linkedin_url = Column(String, nullable=True)
    professional_email = Column(String, nullable=True)

    location = Column(String, nullable=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=True
    )

    company = relationship(
        "Company",
        back_populates="people"
    )