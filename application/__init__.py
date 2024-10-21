from fastapi import FastAPI
from repository.ems.model import ems
from config.database import engine
from controller.auth import auth
from controller.user import user
from controller.department import department
from controller.address import address
from controller.employee import employee

def create_app():
    app = FastAPI()
    ems.Base.metadata.create_all(engine)
    app.include_router(auth.router)
    app.include_router(user.router)
    app.include_router(department.router)
    app.include_router(address.router)
    app.include_router(employee.router)
    return app