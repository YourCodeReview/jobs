from datetime import datetime

from pydantic import BaseModel


class VacancyCreate(BaseModel):
    external_id: int
    company: str
    title: str
    salary: str
    address: str
    requirements: str
    responsibilities: str
    description: str
    date_publication: datetime
