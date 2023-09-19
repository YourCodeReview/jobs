from sqlalchemy.orm import Session
from sqlalchemy import func

from schemas import VacancyCreate
from models import Vacancy


def get_vacancies(db: Session, skip: int = 0, limit: int = 10):
    """ Retrieve all vacancies with pagination """
    vacancies = db.query(Vacancy).offset(skip).limit(limit).all()
    total_count = db.query(func.count(Vacancy.id)).scalar()
    return total_count, vacancies


def get_vacancies_with_specialities(db: Session, skip: int, limit: int, specialities: list):
    """ Retrieve vacancies filtered by speciality along with the total count """
    query = db.query(Vacancy).filter(Vacancy.speciality.in_(specialities))
    total_count = query.count()  # Count the total matching rows
    vacancies = query.offset(skip).limit(limit).all()
    return total_count, vacancies


def get_vacancy_by_id(db: Session, vacancy_id: int):
    """ Retrieve a single vacancy by its ID. """
    return db.query(Vacancy).filter(Vacancy.id == vacancy_id).first()


def create_vacancy(db: Session, vacancy: VacancyCreate):
    """ Create a new vacancy and insert it into the database. """
    db_vacancy = Vacancy(
        external_id=vacancy["id"],
        company_name=vacancy["company_name"],
        title=vacancy["title"],
        salary=vacancy["salary"],
        location=vacancy["location"],
        speciality=vacancy["speciality"],
        internship=vacancy["internship"],
        remote=vacancy["remote"],
        url=vacancy["url"],
        description=vacancy["description"],
    )
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return db_vacancy
