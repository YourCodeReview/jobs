from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import engine
from backend.models import Base
from backend.parsing import api_routes
from backend.api import routes

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

if __name__ == "__main__":
    # import uvicorn
    # uvicorn.run(app, reload=True)
    api_routes.test_vacancy()

    # import subprocess
    # command = "uvicorn main:app --reload"
    # subprocess.call(command, shell=True)
    # api_routes.test_vacancy()
