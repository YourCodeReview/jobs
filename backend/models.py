from sqlalchemy import Column, Integer, String, Boolean, Text

from database import Base


class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, index=True)
    active = Column(Boolean, default=True)
    external_id = Column(Integer, index=True, nullable=True)
    company_name = Column(String, index=True)
    title = Column(String)
    salary = Column(String, nullable=True)
    location = Column(String, nullable=True)
    speciality = Column(String)
    internship = Column(Boolean, default=False)
    remote = Column(Boolean, default=False)
    url = Column(String)
    description = Column(Text)
