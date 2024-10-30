from service.utils.validation_utils import ValidationUtils
from service.utils.response_util import ResponseUtils
from service.services.dept_service import DeptService
from http import HTTPStatus
from sqlalchemy.orm import Session
from redis import Redis

class DeptExecutor:
      def add(request, logged_user, db : Session):
            ValidationUtils.isEmpty(request.name,'name')
            ValidationUtils.isEmpty(request.description, 'description')

            return DeptService.add(request, logged_user,db)
      
      def update(request, db : Session):
            ValidationUtils.isZero(request.id, 'id')
            ValidationUtils.isEmpty(request.name,'name')
            ValidationUtils.isEmpty(request.description, 'description')

            return DeptService.update(request, db)

      def getById(id, db : Session):
            ValidationUtils.isZero(id, 'dept_id')
            return DeptService.getById(id, db)
      
      def fetchById(id, db : Session):
            return DeptService.fetchById(id, db)
      
      
      def deleteById(id, logged_user, db : Session):
            ValidationUtils.isZero(id, 'dept_id')
            return DeptService.deleteById(id, logged_user, db)
      
      def restoreById(id, db : Session):
            ValidationUtils.isZero(id, 'dept_id')
            return DeptService.restoreById(id, db)

      def approveById(id, logged_user, db : Session):
            ValidationUtils.isZero(id, 'dept_id')
            return DeptService.approveById(id, logged_user, db)
      
      
      def getAll(db : Session, cache : Redis):
          return DeptService.getAll(db, cache)
      
      def fetchAll(db : Session, cache : Redis):
          return DeptService.fetchAll(db, cache) 
            