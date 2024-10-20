from repository.ems.service.user_repo_service import UserRepoService
from repository.ems.model.ems import User, Role
from api.dto.dto import SignUpRequest, SignUpResponse, LoginRequest, LoginResponse
from sqlalchemy.orm import Session
from service.utils.message_utils import MessageUtils
from service.utils.response_util import ResponseUtils
from service.mapper.mapper import userModelToUserDtoList
from app_secrets.service.jwt_service import create_access_token
from http import HTTPStatus
from passlib.context import CryptContext
from datetime import timedelta

class UserService:
    def getall(db : Session):
        users = UserRepoService.getAll(db)
        if len(users) == 0: 
            return ResponseUtils.error_wrap(MessageUtils.entities_not_found('Users'), HTTPStatus.NOT_FOUND)
        
        return ResponseUtils.wrap(userModelToUserDtoList(users))