from service.utils.validation_utils import ValidationUtils
from service.utils.response_util import ResponseUtils
from service.services.dept_service import DeptService
from http import HTTPStatus
from sqlalchemy.orm import Session

class DeptExecutor:
      def add(request, logged_user, db : Session):
            try:
                  ValidationUtils.isEmpty(request.name,'name')
                  ValidationUtils.isEmpty(request.description, 'description')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e),HTTPStatus.BAD_REQUEST)

            return DeptService.add(request, logged_user,db)
      
      def update(request, db : Session):
            try:
                  ValidationUtils.isZero(request.id, 'id')
                  ValidationUtils.isEmpty(request.name,'name')
                  ValidationUtils.isEmpty(request.description, 'description')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e),HTTPStatus.BAD_REQUEST)

            return DeptService.update(request, db)

      def getById(id, db : Session):
            try:
                  ValidationUtils.isZero(id, 'dept_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return DeptService.getById(id, db)
      
      def fetchById(id, db : Session):
            return DeptService.fetchById(id, db)
      
      
      def deleteById(id, logged_user, db : Session):
            try:
                  ValidationUtils.isZero(id, 'dept_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return DeptService.deleteById(id, logged_user, db)
      
      def restoreById(id, db : Session):
            try:
                  ValidationUtils.isZero(id, 'dept_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return DeptService.restoreById(id, db)

      def approveById(id, logged_user, db : Session):
            try:
                  ValidationUtils.isZero(id, 'dept_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return DeptService.approveById(id, logged_user, db)
      
      
      def getAll(db : Session):
          return DeptService.getAll(db)
      
      def fetchAll(db : Session):
          return DeptService.fetchAll(db) 
            