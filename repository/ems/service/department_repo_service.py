from repository.ems.model.ems import Department
from sqlalchemy.orm import Session
from config import database
from fastapi import Depends


class DepartmentRepoService:
    def save(dept : Department, db : Session):
        db.add(dept)
        db.commit()

    def getByName(name : str, db : Session):
        return db.query(Department).filter(Department.name == name).first()