from api.dto.dto import AddDepartmentBody, UpdateDepartmentBody, WrappedResponse
from sqlalchemy.orm import Session
from app_secrets.service.jwt_service import decode_token
from fastapi import APIRouter, Depends, Response, Request, status
from service.executor.dept_executor import DeptExecutor
from service.executor.user_executor import UserExecutor
from config import database
from app_secrets.service.dependencies import AccessTokenBearer, RoleChecker
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates 


templates = Jinja2Templates(directory='templates')
router = APIRouter(prefix= '/dept',tags= ['Department'])

get_db = database.get_db
access_token_bearer = AccessTokenBearer()


def redirect_to_login():
    redirect_response = RedirectResponse(url='/auth/login-page', status_code=status.HTTP_302_FOUND)
    redirect_response.delete_cookie(key='access_token')
    return redirect_response

# Pages
@router.get('/department-page')
def render_department_page(request : Request, db : Session = Depends(get_db)):
    access_token = request.cookies.get('access_token')

    
    token_data = decode_token(access_token)

    if token_data is None:
        return redirect_to_login()

    if token_data['role'] != 'ROLE_ADMIN':
       return redirect_to_login()

    return templates.TemplateResponse('department.html', {'request' : request, 'depts' : DeptExecutor.fetchAll(db), 'user' : UserExecutor.fetchByEmail(token_data['sub'], db)})


@router.get('/add-department-page')
def render_add_department_page(request : Request, db : Session = Depends(get_db)):
    access_token = request.cookies.get('access_token')

    
    token_data = decode_token(access_token)

    if token_data is None:
        return redirect_to_login()

    if token_data['role'] != 'ROLE_ADMIN':
       return redirect_to_login()

    return templates.TemplateResponse('add-department.html', {'request' : request})

@router.get('/edit-department-page/{id}')
def render_edit_department_page(id, request : Request, db : Session = Depends(get_db)):
    access_token = request.cookies.get('access_token')

    
    token_data = decode_token(access_token)

    if token_data is None:
        return redirect_to_login()

    if token_data['role'] != 'ROLE_ADMIN':
       return redirect_to_login()

    return templates.TemplateResponse('edit-department.html', {'request' : request, 'dept' : DeptExecutor.fetchById(id, db)})




# API End points

@router.post('', summary= 'Create Department', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def create(request : AddDepartmentBody,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.add(request, tokendetails['sub'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.put('', summary= 'Edit Department', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def update(request : UpdateDepartmentBody,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.update(request, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.get('', summary= 'Get Department by id', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def getById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.getById(id, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.delete('', summary= 'Delete Department by id', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))] )
def deleteById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.deleteById(id, tokendetails['sub'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.patch('/restore', summary= 'Restore Department by id', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def restoreById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.restoreById(id, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.patch('/approve', summary= 'Approve Department by id', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def approveById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.approveById(id, tokendetails['sub'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)


@router.get('/all', summary= 'Get all departments', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def getAll(resp : Response, db : Session = Depends(get_db), _: dict = Depends(access_token_bearer)):
    responseBody = DeptExecutor.getAll(db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)