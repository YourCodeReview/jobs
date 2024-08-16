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
    url: str


class EntityId(BaseModel):
    id: int
