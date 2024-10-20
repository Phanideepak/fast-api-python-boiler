from service.utils.validation_utils import ValidationUtils
from service.utils.response_util import ResponseUtils
from api.dto.dto import SignUpRequest, LoginRequest
from service.services.auth_service import AuthService
from http import HTTPStatus
from sqlalchemy.orm import Session

class AuthExecutor:
      def signup(request : SignUpRequest, db : Session):
            try:
                  ValidationUtils.isEmpty(request.firstname,'firstname')
                  request.firstname = request.firstname.strip()

                  ValidationUtils.isEmpty(request.lastname, 'lastname')
                  request.lastname = request.lastname.strip()

                  ValidationUtils.isEmpty(request.password, 'password')
                  request.password = request.password.strip()

                  ValidationUtils.isEmpty(request.confirm_password, 'confirm_password')
                  request.confirm_password = request.confirm_password.strip()

                  ValidationUtils.isTrue(request.password == request.confirm_password , 'Password and confirm password should be same')

            except Exception as e:
                  return ResponseUtils.error_wrap(str(e),HTTPStatus.BAD_REQUEST)

            return AuthService.signup(request, db)
      

      def signin(request : LoginRequest, db : Session):
            try:
                  ValidationUtils.isEmpty(request.password, 'password')
                  request.password = request.password.strip()

                  ValidationUtils.isEmpty(request.email, 'email')
                  request.email = request.email.strip()

            except Exception as e:
                  return ResponseUtils.error_wrap(str(e),HTTPStatus.BAD_REQUEST)

            return AuthService.signin(request, db)