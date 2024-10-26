from service.services.user_service import UserService
from sqlalchemy.orm import Session

class UserExecutor:
      def getAll(db : Session):
            return UserService.getall(db)
      
      def fetchByEmail(email, db : Session):
            return UserService.fetchByEmail(email, db)