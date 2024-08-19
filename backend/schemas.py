from pydantic import BaseModel, Field


class VacancyCreate(BaseModel):
    external_id: int | None = None
    company_name: str | None = None
    title: str
    salary: str | None = None
    location: str | None = None
    speciality: str
    internship: bool | None = False
    remote: bool | None = False
    url: str | None = None
    description: str | None = None
