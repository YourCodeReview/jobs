from sqlalchemy.orm import Session

from schemas import VacancyCreate
from models import Vacancy


def get_vacancies(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve all vacancies with pagination
    """
    return db.query(Vacancy).offset(skip).limit(limit).all()


def get_vacancy_by_id(db: Session, vacancy_id: int):
    """
    Retrieve a single vacancy by its ID.
    """
    return db.query(Vacancy).filter(Vacancy.id == vacancy_id).first()


def create_vacancy(db: Session, vacancy: VacancyCreate):
    """
    Create a new vacancy and insert it into the database.
    """
    db_vacancy = Vacancy(
        external_id=vacancy["id"],
        title=vacancy["name"],
        salary=str(vacancy["salary"]),
        address=vacancy["address"],
        requirements=vacancy["requirements"],
        responsibilities=vacancy["responsibilities"],
        description=vacancy["description"],
    )
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return db_vacancy
