from repository.ems.service.user_repo_service import UserRepoService
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

        access_token = create_access_token(uid = user.id, username = request.email, expires_delta= timedelta(days=1), role= Role.ROLE_ADMIN.name)
        refresh_token = create_access_token(uid = user.id, username = request.email, expires_delta= timedelta(days=7), role= Role.ROLE_ADMIN.name, refresh = True)

        return ResponseUtils.wrap(SignUpResponse(message = MessageUtils.signup_success_message(), access_token = access_token, refresh_token = refresh_token))

    def signin(request : LoginRequest, db : Session):
        user = UserRepoService.getByEmail(request.email, db)
        if user is None:
            return ResponseUtils.error_wrap(MessageUtils.entity_not_found('User','email', request.email), HTTPStatus.BAD_REQUEST)
        
        if not bcryptContext.verify(request.password, user.password):
            return ResponseUtils.error_wrap(MessageUtils.invalid_password(), HTTPStatus.BAD_REQUEST)
        
        access_token = create_access_token(uid = user.id, username = request.email, expires_delta= timedelta(days=1), role= Role.ROLE_ADMIN.name)
        refresh_token = create_access_token(uid = user.id, username = request.email, expires_delta= timedelta(days=7), role= Role.ROLE_ADMIN.name, refresh = True)

        return ResponseUtils.wrap(LoginResponse(message = MessageUtils.login_success_message(), access_token = access_token, refresh_token = refresh_token))
    


    # def update(request : UpdateDepartmentBody, db : Session):
    #     curr_dept = DepartmentRepoService.getById(request.id, db)

    #     if curr_dept is None:
    #         return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id', request.id), HTTPStatus.INTERNAL_SERVER_ERROR)
        
    #     is_updated = False

    #     if curr_dept.name != request.name:
    #         curr_dept.name = request.name
    #         is_updated = True
        
    #     if curr_dept.description != request.description:
    #         curr_dept.description = request.description
    #         is_updated = True
        
    #     if not is_updated:
    #        return ResponseUtils.error_wrap(MessageUtils.fields_not_modified(), HTTPStatus.BAD_REQUEST) 

    #     try:
    #         DepartmentRepoService.update(curr_dept, db)
    #     except Exception as e:
    #         return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
        
    #     return ResponseUtils.wrap('updated successfully')


    # def getById(id : int, db : Session):
    #     dept = DepartmentRepoService.getById(id, db)
    #     if dept is None:
    #         return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id',id), HTTPStatus.NOT_FOUND)

    #     return ResponseUtils.wrap(departmentModelToDepartmentDto(dept))

    # def deleteById(id : int, db : Session):
    #     dept = DepartmentRepoService.getById(id, db)
    #     if dept is None:
    #         return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id',id), HTTPStatus.NOT_FOUND)
        
    #     if dept.is_deleted:
    #         return ResponseUtils.error_wrap('Already Deleted!', HTTPStatus.BAD_REQUEST)

    #     try:
    #         DepartmentRepoService.softDeleteById(id, db)
    #     except Exception as e:
    #         return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

    #     return ResponseUtils.wrap('Deleted successfully')
    
    # def restoreById(id : int, db : Session):
    #     dept = DepartmentRepoService.getById(id, db)
    #     if dept is None:
    #         return ResponseUtils.error_wrap(MessageUtils.entity_not_found('Department','id',id), HTTPStatus.NOT_FOUND)
        
    #     if not dept.is_deleted:
    #         return ResponseUtils.error_wrap('Already Restored!', HTTPStatus.BAD_REQUEST)

    #     try:
    #         DepartmentRepoService.restoreById(id, db)
    #     except Exception as e:
    #         return ResponseUtils.error_wrap(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

    #     return ResponseUtils.wrap('Restored successfully')
        
    # def getAll(db : Session):
    #     depts = DepartmentRepoService.getAll(db)
    #     if len(depts) == 0:
    #         return ResponseUtils.error_wrap(MessageUtils.entities_not_found('Department'), HTTPStatus.NOT_FOUND)

    #     return ResponseUtils.wrap(departmentModelToDepartmentDtoList(depts))