from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ...database import get_db
from ... import models, schemas


router = APIRouter(
    prefix="/api/v1/people",
    tags=["People"]
)


@router.post("/", response_model=schemas.PersonResponse)
def create_person(
    person: schemas.PersonCreate,
    db: Session = Depends(get_db)
):
    new_person = models.Person(
        full_name=person.full_name,
        normalized_name=person.normalized_name,
        job_title=person.job_title,
        normalized_job_title=person.normalized_job_title,
        linkedin_url=person.linkedin_url,
        professional_email=person.professional_email,
        location=person.location,
        company_id=person.company_id
    )

    db.add(new_person)
    db.commit()
    db.refresh(new_person)

    return new_person


@router.get ("/", response_model=list[schemas.PersonResponse])
def get_people(
    db: Session = Depends(get_db)
):
    people = db.query(models.Person).all()

    return people


@router.get("/{person_id}", response_model=schemas.PersonResponse)
def get_person(
    person_id: int,
    db: Session = Depends(get_db)
):
    person = (
        db.query(models.Person)
        .filter(models.Person.id == person_id)
        .first()
    )

    if person is None:
        raise HTTPException(
            status_code=404,
            detail="Person not found"
        )

    return person