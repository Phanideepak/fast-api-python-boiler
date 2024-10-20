from api.dto.dto import AddDepartmentBody, UpdateDepartmentBody, WrappedResponse
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Response
from service.executor.dept_executor import DeptExecutor
from config import database
from controller.auth.dependencies import AccessTokenBearer, RoleChecker

router = APIRouter(prefix= '/dept',tags= ['Department'])

get_db = database.get_db
access_token_bearer = AccessTokenBearer()

@router.post('', summary= 'Operations related to new data insertion', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def create(request : AddDepartmentBody,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.add(request, tokendetails['uid'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.put('', summary= 'Operations related to new data updation', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def update(request : UpdateDepartmentBody,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.update(request, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.get('', summary= 'Operations related to Get by Id', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def getById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.getById(id, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.delete('', summary= 'Operations related to Delete by Id', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))] )
def deleteById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.deleteById(id, tokendetails['uid'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.patch('/restore', summary= 'Operations related to Restore by Id', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def restoreById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.restoreById(id, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.patch('/approve', summary= 'Operations related to approve by Id', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def restoreById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.approveById(id, tokendetails['uid'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)


@router.get('/all', summary= 'Operations related to Department list', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def getAll(resp : Response, db : Session = Depends(get_db), _: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.getAll(db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)