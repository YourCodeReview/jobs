from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.crud import create_vacancy
from backend.parsing.hh import get_vacancies, main_words, languages_stacks


router = APIRouter()


@router.post("/parse-hh/")
async def save_vacancies_to_db(db: Session = Depends(get_db)):
    result = get_vacancies(main_words, languages_stacks)
    for job in result:
        create_vacancy(db, job)
    return {"message": "Vacancies saved successfully"}
