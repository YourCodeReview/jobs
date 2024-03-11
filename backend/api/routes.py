from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas import VacancyCreate
from crud import create_vacancy, get_vacancies, get_vacancies_with_specialities, get_vacancy_by_id

router = APIRouter()


@router.post("/jobs/", response_model=VacancyCreate)
def new_vacancy(vacancy: VacancyCreate, db: Session = Depends(get_db)):
    return create_vacancy(db, vacancy)


@router.get("/jobs/")
def read_vacancies(
    skip: int = Query(0, description="Offset for pagination"),
    limit: int = Query(10, description="Limit for pagination"),
    specialities: List[str] = Query([], description="List of specialities to filter by, separated by '&'"),
    db: Session = Depends(get_db)
):
    if specialities:
        if specialities == ['data']:
            specialities.extend(['data scientist', 'data science', 'аналитик данных', 'ml'])
        total_count, vacancies = get_vacancies_with_specialities(db, skip, limit, specialities)
    else:
        total_count, vacancies = get_vacancies(db, skip, limit)

    return {
        "total_count": total_count,
        "data": vacancies,
    }


@router.get("/jobs/{vacancy_id}")
def read_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    vacancy = get_vacancy_by_id(db, vacancy_id)
    if vacancy is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return vacancy

###################################
import httpx


@router.post("/subscribe")
async def subscribe(api_key: str, email: str):
    target_url = "https://api.unisender.com/ru/api/subscribe"
    headers = {
        "Content-Type": "application/json",
    }

    params = {
        "api_key": api_key,
        "format": "json",
        "list_ids": 244,
        "double_optin": 3,
        "fields[email]": email,
    }
    import requests
    req = requests.post(target_url, params=params)
    print(req.content)
