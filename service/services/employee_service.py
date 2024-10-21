from repository.ems.service.employment_repo_service import EmployeeRepoService
from repository.ems.service.department_repo_service import DepartmentRepoService
from repository.ems.service.user_repo_service import UserRepoService
from repository.ems.model.ems import Employee, User,Role
from api.dto.dto import AddEmployeeRequest, UpdateEmployeeRequest
from sqlalchemy.orm import Session
from service.utils.message_utils import MessageUtils
from service.utils.response_util import ResponseUtils
from service.mapper.mapper import departmentModelToDepartmentDto, departmentModelToDepartmentDtoList, employeeModelToEmployeeDto
from http import HTTPStatus
from passlib.context import CryptContext
from datetime import datetime

bcryptContext = CryptContext(schemes=['bcrypt'])

class EmployeeService:
    def add(request : AddEmployeeRequest, logged_user, role, db : Session):
        user = UserRepoService.getByEmail(logged_user, db)
        dept = DepartmentRepoService.getById(request.dept_id, db)
        
        if dept is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id', request.dept_id), HTTPStatus.NOT_FOUND)

        if role == 'ROLE_ADMIN' and dept.name != 'HR':
            return ResponseUtils.error_wrap('Admin Users can only recruit HR Employees', HTTPStatus.BAD_REQUEST)
        
        if role == 'ROLE_HR' and dept.name == 'HR':
            return ResponseUtils.error_wrap('HR Users cannot recruit HR Employees', HTTPStatus.BAD_REQUEST)


        try:
            EmployeeRepoService.save(Employee(firstname = request.firstname, lastname = request.lastname, designation = request.designation, contact = request.contact, created_by = user.id, dept_id = dept.id, eid = request.eid), db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
        
        return ResponseUtils.wrap('added successfully')
    

    def update(request : UpdateEmployeeRequest, logged_user, role, db : Session):
        user = UserRepoService.getByEmail(logged_user, db)
        emp = EmployeeRepoService.getByEid(request.eid, db)

        if emp is None:
            return  ResponseUtils.error_wrap(MessageUtils.entity_not_found('Employee','eid', request.eid), HTTPStatus.NOT_FOUND)

        curr_dept = DepartmentRepoService.getById(emp.dept_id, db)

        if curr_dept is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id', request.id), HTTPStatus.NOT_FOUND)
        
        

        if role == 'ROLE_ADMIN' and curr_dept.name != 'HR':
            return ResponseUtils.error_wrap('Admin Users can only edit HR Employees', HTTPStatus.BAD_REQUEST)
        
        if role == 'ROLE_HR' and curr_dept.name == 'HR':
            return ResponseUtils.error_wrap('HR Users cannot edit HR Employees', HTTPStatus.BAD_REQUEST)
        
        is_updated = False

        if request.firstname != emp.firstname:
            emp.firstname = request.firstname
            is_updated = True
        
        if request.lastname != emp.lastname:
            emp.lastname = request.lastname
            is_updated = True

        if request.contact != emp.contact:
            emp.contact = request.contact
            is_updated = True
        
        if request.dept_id != emp.dept_id:
            emp.dept_id = request.dept_id
            is_updated = True
        
        if not is_updated:
           return ResponseUtils.error_wrap(MessageUtils.fields_not_modified(), HTTPStatus.BAD_REQUEST) 

        try:
            EmployeeRepoService.update(emp, db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
        
        return ResponseUtils.wrap('updated successfully')


    def getById(id : int, db : Session):
        emp = EmployeeRepoService.getById(id, db)

        if emp is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Employee','id',id), HTTPStatus.NOT_FOUND)

        dept = DepartmentRepoService.getById(emp.dept_id, db)

        if dept is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id',id), HTTPStatus.NOT_FOUND)

        return ResponseUtils.wrap(employeeModelToEmployeeDto(emp, dept, UserRepoService.getById(emp.created_by, db), UserRepoService.getById(emp.deleted_by, db), UserRepoService.getById(emp.approved_by, db) ))


    def deleteById(id : int, logged_user, db : Session):
        user = UserRepoService.getByEmail(logged_user, db)
        emp = EmployeeRepoService.getById(id, db)
        if emp is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Employee','id',id), HTTPStatus.NOT_FOUND)
        
        if emp.is_deleted:
            return ResponseUtils.error_wrap('Already Deleted!', HTTPStatus.BAD_REQUEST)

        try:
            EmployeeRepoService.softDeleteById(id, user.id, db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

        return ResponseUtils.wrap('Deleted successfully')
    
    def restoreById(id : int, db : Session):
        emp = EmployeeRepoService.getById(id, db)
        if emp is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Employee','id',id), HTTPStatus.NOT_FOUND)
        
        if not emp.is_deleted:
            return ResponseUtils.error_wrap('Already Restored!', HTTPStatus.BAD_REQUEST)

        try:
            EmployeeRepoService.restoreById(id, db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

        return ResponseUtils.wrap('Restored successfully')
    
    def approveById(id : int, logged_user, role, db : Session):   
        user = UserRepoService.getByEmail(logged_user, db)    
        emp = EmployeeRepoService.getById(id, db)

        if emp is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Employee','id',id), HTTPStatus.NOT_FOUND)
        
        dept = DepartmentRepoService.getById(emp.dept_id, db)
        
        if dept is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id', emp.dept_id), HTTPStatus.NOT_FOUND)

        if role == 'ROLE_ADMIN' and dept.name != 'HR':
            return ResponseUtils.error_wrap('Admin Users can only approve HR Employees', HTTPStatus.BAD_REQUEST)
        
        if role == 'ROLE_HR' and dept.name == 'HR':
            return ResponseUtils.error_wrap('HR Users cannot approve HR Employees', HTTPStatus.BAD_REQUEST)
    

        if emp.is_approved:
            return ResponseUtils.error_wrap('Already Approved!', HTTPStatus.BAD_REQUEST)


        emp_role = 'ROLE_EMPLOYEE'

        if role == 'ROLE_ADMIN':
            emp_role = 'ROLE_HR'

        try:
            emp.office_mail = f'{emp.firstname}.{emp.lastname}.{emp.eid}@lincom.com'
            emp.is_approved = True
            emp.approved_at = datetime.now()
            emp.approved_by = user.id

            EmployeeRepoService.update(emp, db)
            
            UserRepoService.save(User(firstname = emp.firstname, lastname = emp.lastname, email = emp.office_mail, password = bcryptContext.hash('abc@123'), role = emp_role), db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

        return ResponseUtils.wrap('approved successfully')


    def getAll(db : Session):
        emps = EmployeeRepoService.getAll(db)
        if len(emps) == 0:
            return ResponseUtils.error_wrap(MessageUtils.entities_not_found('Employee'), HTTPStatus.NOT_FOUND)


        empDtos = []

        for emp in emps:
            empDtos.append(employeeModelToEmployeeDto(emp, DepartmentRepoService.getById(emp.dept_id, db), UserRepoService.getById(emp.created_by, db), UserRepoService.getById(emp.deleted_by, db), UserRepoService.getById(emp.approved_by, db) ))

        return ResponseUtils.wrap(empDtos)