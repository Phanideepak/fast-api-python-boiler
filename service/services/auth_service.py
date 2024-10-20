from repository.ems.service.user_repo_service import UserRepoService
from repository.ems.service.employment_repo_service import EmployeeRepoService
from repository.ems.model.ems import User, Role
from api.dto.dto import SignUpRequest, SignUpResponse, LoginRequest, LoginResponse
from sqlalchemy.orm import Session
from service.utils.message_utils import MessageUtils
from service.utils.response_util import ResponseUtils
from app_secrets.service.jwt_service import create_access_token
from http import HTTPStatus
from passlib.context import CryptContext
from datetime import timedelta

bcryptContext = CryptContext(schemes=['bcrypt'])

class AuthService:
    def signup(request : SignUpRequest, db : Session):
        if UserRepoService.getByEmail(request.email, db) is not None:
            return ResponseUtils.error_wrap(MessageUtils.entity_already_exists('User','email', request.email), HTTPStatus.BAD_REQUEST)
        try:
            UserRepoService.save(User(email = request.email,firstname = request.firstname, lastname = request.lastname, password = bcryptContext.hash(request.password), role = Role.ROLE_ADMIN), db)
        except Exception as e:
            return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
        
        user = UserRepoService.getByEmail(request.email, db)

        access_token = create_access_token(username = request.email, expires_delta= timedelta(days=1), role= Role.ROLE_ADMIN.name)
        refresh_token = create_access_token(username = request.email, expires_delta= timedelta(days=7), role= Role.ROLE_ADMIN.name, refresh = True)

        return ResponseUtils.wrap(SignUpResponse(message = MessageUtils.signup_success_message(), access_token = access_token, refresh_token = refresh_token))

    def signin(request : LoginRequest, db : Session):
        user = UserRepoService.getByEmail(request.email, db)
        if user is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('User','email', request.email), HTTPStatus.BAD_REQUEST)
        
        if not bcryptContext.verify(request.password, user.password):
            return ResponseUtils.error_wrap(MessageUtils.invalid_password(), HTTPStatus.BAD_REQUEST)

        access_token = create_access_token(username = request.email, expires_delta= timedelta(days=1), role= user.role.name)
        refresh_token = create_access_token(username = request.email, expires_delta= timedelta(days=7), role= user.role.name, refresh = True)

        return ResponseUtils.wrap(LoginResponse(message = MessageUtils.login_success_message(), access_token = access_token, refresh_token = refresh_token))