from sqlalchemy.orm import Session
from fastapi import Depends
from repository.ems.model.ems import Employee
from datetime import datetime


class EmployeeRepoService:
    def save(employee : Employee, db : Session):
        db.add(employee)
        db.commit()
    
    def update(employee : Employee, db : Session):
        db.query(Employee).filter(Employee.id == employee.id).update({
                                      Employee.firstname : employee.firstname,
                                      Employee.lastname : employee.lastname,  
                                      Employee.office_mail : employee.office_mail, 
                                      Employee.contact : employee.contact,
                                      Employee.dept_id : employee.dept_id,
                                      Employee.created_by : employee.created_by,
                                      Employee.approved_at : employee.approved_at,
                                      Employee.approved_by : employee.approved_by,
                                      Employee.is_approved : employee.is_approved  
                                      })
        db.commit()

    def getByEid(eid : str, db : Session):
        return db.query(Employee).filter(Employee.eid == eid).first()
    
    def getByOfficeMail(office_mail : str, db : Session):
        return db.query(Employee).filter(Employee.office_mail == office_mail).first()
    
    def getById(id : int, db : Session):
        return db.query(Employee).filter(Employee.id == id).first()
    
    def softDeleteById(id : int, uid : int, db : Session):
        db.query(Employee).filter(Employee.id == id).update({Employee.is_deleted : True, Employee.deleted_by : uid, Employee.deleted_at : datetime.now()})
        db.commit()
    
    def restoreById(id : int, db : Session):
        db.query(Employee).filter(Employee.id == id).update({Employee.is_deleted : False, Employee.deleted_at : None, Employee.deleted_by : None})
        db.commit()
    
    def approveById(id : int, uid : int, db : Session):
        db.query(Employee).filter(Employee.id == id).update({Employee.is_approved : True, Employee.approved_at : datetime.now(), Employee.approved_by : uid})
        db.commit()
    
    def getAll(db : Session):
        return db.query(Employee).filter(Employee.is_deleted == False).all()