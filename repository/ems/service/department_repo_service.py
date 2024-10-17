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
    
    def getById(id : int, db : Session):
        return db.query(Department).filter(Department.id == id).first()
    
    def deleteById(id: int, db : Session):
        db.query(Department).filter(Department.id == id).delete()
        db.commit()
    
    def getAll(db : Session):
        return db.query(Department).filter(Department.is_deleted == False).all()