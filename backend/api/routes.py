from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas import VacancyCreate
from crud import create_vacancy, get_vacancies, get_vacancy_by_id


router = APIRouter()


LIMIT_DEFAULT = 10
SKIP_DEFAULT = 0

DATA_JOBS = ["data scientist", "data science", "аналитик данных", "ml"]

INTERNSHIP = "Filter by internship availability"
LIMIT = "Limit for pagination"
LOCATION = "List of locations to filter by"
REMOTE = "Filter by remote ability"
SKIP = "Offset for pagination"
SPECIALITIES = "List of specialities to filter by, separated by '&"

NOT_FOUND = "Job not found"


@router.post("/jobs/", response_model=VacancyCreate)
def new_vacancy(vacancy: VacancyCreate, db: Session = Depends(get_db)):
    return create_vacancy(db, vacancy)


@router.get("/jobs/")
def read_vacancies(
    skip: int = Query(SKIP_DEFAULT, description=SKIP),
    limit: int = Query(LIMIT_DEFAULT, description=LIMIT),
    specialities: list[str] = Query([], description=SPECIALITIES),
    internship: Optional[bool] = Query(None, description=INTERNSHIP),
    remote: Optional[bool] = Query(None, description=REMOTE),
    location: Optional[list[str]] = Query([], description=LOCATION),
    db: Session = Depends(get_db)
):
    if specialities and 'data' in specialities:
        specialities.extend(DATA_JOBS)
    total_count, vacancies = get_vacancies(
        db,
        skip,
        limit,
        specialities=specialities,
        internship=internship,
        remote=remote,
        location=location,
        )
    return {
        "total_count": total_count,
        "data": vacancies,
    }


@router.get("/jobs/{vacancy_id}")
def read_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    vacancy = get_vacancy_by_id(db, vacancy_id)
    if not vacancy:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=NOT_FOUND
        )
    return vacancy
