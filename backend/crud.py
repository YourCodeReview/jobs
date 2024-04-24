from sqlalchemy.orm import Session

from schemas import VacancyCreate
from models import Vacancy


def get_vacancies(
        db: Session,
        skip: int,
        limit: int,
        specialities: list[str],
        internship: bool,
        remote: bool,
        locations: list[str]

):
    """ Retrieve filtred vacancies """
    query = db.query(Vacancy)
    if specialities:
        query = query.filter(Vacancy.speciality.in_(specialities))
    if internship:
        query = query.filter(Vacancy.internship)
    if remote:
        query = query.filter(Vacancy.remote)
    if locations:
        query = query.filter(Vacancy.location.in_(locations))
    vacancies = query.offset(skip).limit(limit).all()
    total_count = query.count()
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
