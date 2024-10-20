from service.utils.validation_utils import ValidationUtils
from service.utils.response_util import ResponseUtils
from api.dto.dto import SignUpRequest, LoginRequest
from service.services.user_service import UserService
from http import HTTPStatus
from sqlalchemy.orm import Session

class UserExecutor:
      def getAll(db : Session):
            return UserService.getall(db)