from repository.ems.service.department_repo_service import DepartmentRepoService
from repository.ems.service.user_repo_service import UserRepoService
from repository.ems.model.ems import Department
from api.dto.dto import AddDepartmentBody,UpdateDepartmentBody
from sqlalchemy.orm import Session
from service.utils.message_utils import MessageUtils
from service.utils.response_util import ResponseUtils
from service.mapper.mapper import departmentModelToDepartmentDto, departmentModelToDepartmentDtoList
from http import HTTPStatus

class DeptService:
    def add(request : AddDepartmentBody, logged_user, db : Session):
        user = UserRepoService.getByEmail(logged_user, db)
        if DepartmentRepoService.getByName(request.name, db) is not None:
            return ResponseUtils.error_wrap(MessageUtils.entity_already_exists('Department','name', request.name), HTTPStatus.BAD_REQUEST)
        try:
            DepartmentRepoService.save(Department(name= request.name, description = request.description, created_by = user.id), db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
        
        return ResponseUtils.wrap('added successfully')
    

    def update(request : UpdateDepartmentBody, db : Session):
        curr_dept = DepartmentRepoService.getById(request.id, db)

        if curr_dept is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id', request.id), HTTPStatus.INTERNAL_SERVER_ERROR)
        
        is_updated = False

        if curr_dept.name != request.name:
            curr_dept.name = request.name
            is_updated = True
        
        if curr_dept.description != request.description:
            curr_dept.description = request.description
            is_updated = True
        
        if not is_updated:
           return ResponseUtils.error_wrap(MessageUtils.fields_not_modified(), HTTPStatus.BAD_REQUEST) 

        try:
            DepartmentRepoService.update(curr_dept, db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
        
        return ResponseUtils.wrap('updated successfully')


    def getById(id : int, db : Session):
        dept = DepartmentRepoService.getById(id, db)
        if dept is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id',id), HTTPStatus.NOT_FOUND)

        return ResponseUtils.wrap(departmentModelToDepartmentDto(dept))

    def deleteById(id : int, logged_user, db : Session):
        user = UserRepoService.getByEmail(logged_user, db)
        dept = DepartmentRepoService.getById(id, db)
        if dept is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id',id), HTTPStatus.NOT_FOUND)
        
        if dept.is_deleted:
            return ResponseUtils.error_wrap('Already Deleted!', HTTPStatus.BAD_REQUEST)

        try:
            DepartmentRepoService.softDeleteById(id, user.id, db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

        return ResponseUtils.wrap('Deleted successfully')
    
    def restoreById(id : int, db : Session):
        dept = DepartmentRepoService.getById(id, db)
        if dept is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id',id), HTTPStatus.NOT_FOUND)
        
        if not dept.is_deleted:
            return ResponseUtils.error_wrap('Already Restored!', HTTPStatus.BAD_REQUEST)

        try:
            DepartmentRepoService.restoreById(id, db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

        return ResponseUtils.wrap('Restored successfully')
    
    def approveById(id : int, logged_user, db : Session):
        user = UserRepoService.getByEmail(logged_user, db)
        dept = DepartmentRepoService.getById(id, db)
        if dept is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id',id), HTTPStatus.NOT_FOUND)
        
        if dept.is_approved:
            return ResponseUtils.error_wrap('Already Approved!', HTTPStatus.BAD_REQUEST)

        try:
            DepartmentRepoService.approveById(id, user.id, db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

        return ResponseUtils.wrap('Restored successfully')


    def getAll(db : Session):
        depts = DepartmentRepoService.getAll(db)
        if len(depts) == 0:
            return ResponseUtils.error_wrap(MessageUtils.entities_not_found('Department'), HTTPStatus.NOT_FOUND)

        return ResponseUtils.wrap(departmentModelToDepartmentDtoList(depts))