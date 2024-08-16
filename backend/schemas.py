from pydantic import BaseModel


class VacancyCreate(BaseModel):
    # external_id: int
    company: str
    title: str
    salary: str
    address: str | None
    requirements: str | None
    responsibilities: str | None
    specialty: str | None
    description: str
    employment: str | None
    schedule: str | None
    url: str


class EntityId(BaseModel):
    id: int
