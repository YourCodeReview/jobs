from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Base
from parsing import api_routes
from api import routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://68.183.220.246",
    "https://68.183.220.246",
    "http://68.183.220.246:80",
    "https://68.183.220.246:80",
    "http://localhost:80",
    "https://localhost:80",
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost",
    "https://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router, prefix="/api", tags=["API"])
app.include_router(api_routes.router, prefix="/parse", tags=["Parsing"])


def import_vacancies():
    from database import get_db
    from crud import create_vacancy
    from parsing.hh import get_vacancies, main_words, languages_stacks
    
    result = get_vacancies(main_words, languages_stacks)
    for db in get_db():
        for job in result:
            create_vacancy(db, job)


if __name__ == "__main__":
    import_vacancies()