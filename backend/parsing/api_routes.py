from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from crud import create_vacancy
from .hh import get_vacancies



router = APIRouter()


@router.post("/parse/parse-hh/")
async def save_vacancies_to_db(db: Session = Depends(get_db)):
    result = get_vacancies(main_words, languages_stacks)
    for job in result:
        create_vacancy(db, job)
    return {"message": "Vacancies saved successfully"}


def test_vacancy():
    result = get_vacancies(main_words, languages_stacks)
    for db in get_db():
        for job in result:
            create_vacancy(db, job)

test_vacancy()