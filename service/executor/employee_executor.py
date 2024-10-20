from service.utils.validation_utils import ValidationUtils
from service.utils.response_util import ResponseUtils
from service.services.employee_service import EmployeeService
from http import HTTPStatus
from api.dto.dto import AddEmployeeRequest, UpdateEmployeeRequest
from sqlalchemy.orm import Session



class EmployeeExecutor:
      def add(request : AddEmployeeRequest, logged_user, role, db : Session):
            try:
                  ValidationUtils.isEmpty(request.firstname, 'firstname')
                  ValidationUtils.isEmpty(request.lastname, 'lastname')
                  ValidationUtils.isEmpty(request.contact, 'contact')
                  ValidationUtils.isEmpty(request.eid, 'eid')
                  ValidationUtils.isZero(request.dept_id, 'dept_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e),HTTPStatus.BAD_REQUEST)

            return EmployeeService.add(request, logged_user, role, db)
      
      def update(request, logged_user, role, db : Session):
            try:
                  ValidationUtils.isEmpty(request.firstname, 'firstname')
                  ValidationUtils.isEmpty(request.lastname, 'lastname')
                  ValidationUtils.isEmpty(request.contact, 'contact')
                  ValidationUtils.isEmpty(request.eid, 'eid')
                  ValidationUtils.isZero(request.dept_id, 'dept_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e),HTTPStatus.BAD_REQUEST)

            return EmployeeService.update(request, logged_user, role, db)

      def getById(id, db : Session):
            try:
                  ValidationUtils.isZero(id, 'employee_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return EmployeeService.getById(id, db)
      
      def deleteById(id, logged_user, db : Session):
            try:
                  ValidationUtils.isZero(id, 'employee_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return EmployeeService.deleteById(id, logged_user, db)
      
      def restoreById(id, db : Session):
            try:
                  ValidationUtils.isZero(id, 'employee_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return EmployeeService.restoreById(id, db)

      def approveById(id, logged_user, role, db : Session):
            try:
                  ValidationUtils.isZero(id, 'employee_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return EmployeeService.approveById(id, logged_user, role, db)
      
      
      def getAll(db : Session):
          return EmployeeService.getAll(db)
            