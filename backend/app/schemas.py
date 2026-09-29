from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    normalized_name: str
    domain: str | None = None
    linkedin_url: str | None = None
    industry: str | None = None
    country: str | None = None


class CompanyResponse(BaseModel):
    id: int
    name: str
    normalized_name: str
    domain: str | None = None
    linkedin_url: str | None = None
    industry: str | None = None
    country: str | None = None

    class Config:
        from_attributes = True

class PersonCreate(BaseModel):
    full_name: str
    normalized_name: str

    job_title: str | None = None
    normalized_job_title: str | None = None

    linkedin_url: str | None = None
    professional_email: str | None = None

    location: str | None = None
    company_id: int | None = None


class PersonResponse(BaseModel):
    id: int
    full_name: str
    normalized_name: str

    job_title: str | None = None
    normalized_job_title: str | None = None

    linkedin_url: str | None = None
    professional_email: str | None = None

    location: str | None = None
    company_id: int | None = None

    class Config:
        from_attributes = True