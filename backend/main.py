from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Base
from api import routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://jobs.yourcodereview.com",
    "https://jobs.yourcodereview.com",
    "http://jobs.yourcodereview.com:80",
    "https://jobs.yourcodereview.com:443",
    "http://68.183.220.246",
    "https://68.183.220.246",
    "http://68.183.220.246:80",
    "https://68.183.220.246:443",
    "http://localhost:80",
    "https://localhost:443",
    "http://localhost:3000",
    "https://localhost:3000",
    "https://localhost:4443",
    "http://localhost",
    "https://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(routes.router, prefix="/api", tags=["API"])
