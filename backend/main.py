from fastapi import FastAPI

from database import engine
from models import Base
from parsing import api_routes
from api import routes


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(routes.router, prefix="/api", tags=["API"])
app.include_router(api_routes.router, prefix="/parse", tags=["Parsing"])
