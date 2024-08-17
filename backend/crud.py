from sqlalchemy.orm import Session
from sqlalchemy import func, desc

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
    """ Retrieve filtred vacancies. """
    query = db.query(Vacancy)
    if specialities:
        query = query.filter(Vacancy.speciality.in_(specialities))
    if internship:
        query = query.filter(Vacancy.internship)
    if remote:
        query = query.filter(Vacancy.remote)
    if locations:
        query = query.filter(Vacancy.location.in_(locations))
    return query.count(), query.offset(skip).limit(limit).all()

def get_vacancies_with_specialities(db: Session, skip: int, limit: int, specialities: list):
    """ Retrieve vacancies filtered by speciality along with the total count """
    query = db.query(Vacancy).filter(Vacancy.speciality.in_(specialities)).order_by(desc(Vacancy.date_publication))
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
        date_publication=vacancy.get("date_publication", None),
    )
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return db_vacancy


def get_locations(db: Session):
    """ Retrieve list of all locations. """
    locations = db.query(Vacancy.location).distinct()
    return locations.count(), [location[0] for location in locations]
