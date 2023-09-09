from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from crud import create_vacancy
from .hh import fetch_hh_vacancies


router = APIRouter()


@router.post("/parse-hh/")
async def save_vacancies_to_db(db: Session = Depends(get_db)):
    jobs = fetch_hh_vacancies("junior python")
    for job in jobs:
        create_vacancy(db, job)
    return {"message": "Vacancies saved successfully"}
