from fastapi import FastAPI
from repository.ems.model import ems
from config.database import engine
from controller.auth import auth
from controller.user import user
from controller.department import department

def create_app():
    app = FastAPI()
    ems.Base.metadata.create_all(engine)
    app.include_router(auth.router)
    app.include_router(user.router)
    app.include_router(department.router)
    return app