from api.dto.dto import AddEmployeeRequest, UpdateEmployeeRequest
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Response, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from service.executor.employee_executor import EmployeeExecutor
from service.executor.user_executor import UserExecutor
from service.executor.dept_executor import DeptExecutor
from config import database, redis
from redis import Redis
from controller.common.common import redirect_to_login
from app_secrets.service.dependencies import AccessTokenBearer, RoleChecker
from app_secrets.service.jwt_service import decode_token


router = APIRouter(prefix= '/emp',tags= ['Employee'])
templates = Jinja2Templates(directory='templates')

get_db = database.get_db
get_cache = redis.get_redis
access_token_bearer = AccessTokenBearer()


@router.get('/employee-page')
def render_employee_page(request : Request, db : Session = Depends(get_db)):
    access_token = request.cookies.get('access_token')

    
    token_data = decode_token(access_token)

    if token_data is None:
        return redirect_to_login()

    if token_data['role'] not in ['ROLE_ADMIN','ROLE_HR']:
       return redirect_to_login()

    return templates.TemplateResponse('employee.html', {'request' : request, 'emps' : EmployeeExecutor.fetchAll(db), 'user' : UserExecutor.fetchByEmail(token_data['sub'], db)})

@router.get('/add-employee-page')
def render_add_employee_page(request : Request, db : Session = Depends(get_db), cache  : Redis = Depends(get_cache)):
    access_token = request.cookies.get('access_token')

    
    token_data = decode_token(access_token)

    if token_data is None:
        return redirect_to_login()

    if token_data['role'] not in ['ROLE_ADMIN','ROLE_HR']:
       return redirect_to_login()

    return templates.TemplateResponse('add-employee.html', {'request' : request, 'depts' : DeptExecutor.fetchAll(db, cache), 'user' : UserExecutor.fetchByEmail(token_data['sub'], db) })

@router.get('/edit-employee-page/{id}')
def render_edit_employee_page(id, request : Request, db : Session = Depends(get_db), cache  : Redis = Depends(get_cache)):
    access_token = request.cookies.get('access_token')

    
    token_data = decode_token(access_token)

    if token_data is None:
        return redirect_to_login()

    if token_data['role'] not in ['ROLE_ADMIN','ROLE_HR']:
       return redirect_to_login()

    return templates.TemplateResponse('edit-employee.html', {'request' : request, 'emp' : EmployeeExecutor.fetchById(id, db), 'depts' : DeptExecutor.fetchAll(db, cache), 'user' : UserExecutor.fetchByEmail(token_data['sub'], db)})




# API End Points

@router.post('', summary= 'Onboard Employee', dependencies=[Depends(RoleChecker(['ROLE_ADMIN', 'ROLE_HR']))])
def create(request : AddEmployeeRequest,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = EmployeeExecutor.add(request, tokendetails['sub'], tokendetails['role'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.put('', summary= 'Edit Employee Details', dependencies=[Depends(RoleChecker(['ROLE_ADMIN','ROLE_HR']))])
def update(request : UpdateEmployeeRequest,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = EmployeeExecutor.update(request, tokendetails['sub'], tokendetails['role'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.get('', summary= 'Get Employee by id', dependencies=[Depends(RoleChecker(['ROLE_ADMIN','ROLE_EMPLOYEE','ROLE_HR','ROLE_FINANCE']))])
def getById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = EmployeeExecutor.getById(id, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.delete('', summary= 'Delete Employee by id', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))] )
def deleteById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = EmployeeExecutor.deleteById(id, tokendetails['sub'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.patch('/restore', summary= 'Restore Employee', dependencies=[Depends(RoleChecker(['ROLE_HR']))])
def restoreById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = EmployeeExecutor.restoreById(id, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.patch('/approve', summary= 'Approve Employee by Id', dependencies=[Depends(RoleChecker(['ROLE_HR','ROLE_ADMIN']))])
def approveById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = EmployeeExecutor.approveById(id, tokendetails['sub'], tokendetails['role'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)


@router.get('/all', summary= 'Get all employees', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def getAll(resp : Response, db : Session = Depends(get_db), _: dict = Depends(access_token_bearer)):
    responseBody = EmployeeExecutor.getAll(db)

    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)