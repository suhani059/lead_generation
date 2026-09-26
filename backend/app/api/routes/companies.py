from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import get_db
from ... import models, schemas


router = APIRouter(
    prefix="/api/v1/companies",
    tags=["Companies"]
)


@router.post("/", response_model=schemas.CompanyResponse)
def create_company(
    company: schemas.CompanyCreate,
    db: Session = Depends(get_db)
):
    new_company = models.Company(
        name=company.name,
        normalized_name=company.normalized_name,
        domain=company.domain,
        linkedin_url=company.linkedin_url,
        industry=company.industry,
        country=company.country
    )

    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company