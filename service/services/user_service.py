from repository.ems.service.user_repo_service import UserRepoService
from sqlalchemy.orm import Session
from service.utils.message_utils import MessageUtils
from service.utils.response_util import ResponseUtils
from service.mapper.mapper import userModelToUserDtoList, userModelToUserDto
from http import HTTPStatus

class UserService:
    def getall(db : Session):
        users = UserRepoService.getAll(db)
        if len(users) == 0: 
            return ResponseUtils.error_wrap(MessageUtils.entities_not_found('Users'), HTTPStatus.NOT_FOUND)
        
        return ResponseUtils.wrap(userModelToUserDtoList(users))
    
    def fetchByEmail(email, db : Session):
        return userModelToUserDto(UserRepoService.getByEmail(email, db))