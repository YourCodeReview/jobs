from sqlalchemy import Column, Integer, String, Text

from database import Base


class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(Integer, index=True, nullable=True)
    company = Column(String, index=True, nullable=True)
    title = Column(String)
    salary = Column(String)
    address = Column(String, nullable=True)
    requirements = Column(String)
    responsibilities = Column(String)
    description = Column(Text)
