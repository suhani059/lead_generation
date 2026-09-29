from fastapi import APIRouter, Depends, HTTPException
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
    existing_company = (
        db.query(models.Company)
        .filter(
            models.Company.normalized_name == company.normalized_name
        )
        .first()
    )

    if existing_company:
        return existing_company
    
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

@router.get("/", response_model=list[schemas.CompanyResponse])
def get_companies(
    db: Session = Depends(get_db)
):
    companies = db.query(models.Company).all()

    return companies

@router.get("/{company_id}", response_model=schemas.CompanyResponse)
def get_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    company = (
        db.query(models.Company)
        .filter(models.Company.id == company_id)
        .first()
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return company

