from repository.ems.service.user_repo_service import UserRepoService
from sqlalchemy.orm import Session
from service.utils.message_utils import MessageUtils
from service.utils.response_util import ResponseUtils
from service.mapper.mapper import userModelToUserDtoList, userModelToUserDto
from http import HTTPStatus

class UserService:
    def getAll(db : Session):
        return ResponseUtils.wrap(userModelToUserDtoList(UserRepoService.validateAndGetAll(db)))
    
    def fetchByEmail(email, db : Session):
        return userModelToUserDto(UserRepoService.fetchByEmail(email, db))