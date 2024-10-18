from fastapi import FastAPI
from repository.ems.model import ems
from config.database import engine
from controller.department import department 

def create_app():
    app = FastAPI()
    ems.Base.metadata.create_all(engine)
    app.include_router(department.router)
    return app