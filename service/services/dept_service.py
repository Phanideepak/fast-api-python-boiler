from repository.ems.service.department_repo_service import DepartmentRepoService
from repository.ems.model.ems import Department
from api.dto.dto import AddDepartmentBody
from sqlalchemy.orm import Session
from service.utils.response_util import ResponseUtils
from http import HTTPStatus

class DeptService:
    def add(request : AddDepartmentBody, db : Session):
        if DepartmentRepoService.getByName(request.name, db) is not None:
            return ResponseUtils.error_wrap('Already Exists', HTTPStatus.INTERNAL_SERVER_ERROR)
        try:
            DepartmentRepoService.save(Department(name= request.name, description = request.description), db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
        
        return ResponseUtils.wrap('added successfully')