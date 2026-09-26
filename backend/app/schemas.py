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