from api.dto.dto import AddAddressRequest, UpdateAddressRequest
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Response, Request
from controller.common.common import redirect_to_login
from app_secrets.service.jwt_service import decode_token
from fastapi.templating import Jinja2Templates
from service.executor.address_executor import AddressExecutor
from service.executor.user_executor import UserExecutor
from config import database
from app_secrets.service.dependencies import AccessTokenBearer, RoleChecker

router = APIRouter(prefix= '/address',tags= ['Address'])

templates = Jinja2Templates(directory='templates')
get_db = database.get_db
access_token_bearer = AccessTokenBearer()



# Pages

@router.get('/address-page')
def render_address_page(request : Request, db : Session = Depends(get_db)):
    access_token = request.cookies.get('access_token')

    
    token_data = decode_token(access_token)

    if token_data is None:
        return redirect_to_login()

    if token_data['role'] != 'ROLE_EMPLOYEE':
       return redirect_to_login()

    return templates.TemplateResponse('address.html', {'request' : request, 'addresses' : AddressExecutor.fetchAll(token_data['sub'], db), 'user' : UserExecutor.fetchByEmail(token_data['sub'], db)})


@router.get('/add-address-page')
def render_add_address_page(request : Request, db : Session = Depends(get_db)):
    access_token = request.cookies.get('access_token')

    
    token_data = decode_token(access_token)

    if token_data is None:
        return redirect_to_login()

    if token_data['role'] != 'ROLE_EMPLOYEE':
       return redirect_to_login()

    return templates.TemplateResponse('add-address.html', {'request' : request, 'user' : UserExecutor.fetchByEmail(token_data['sub'], db)})


@router.get('/edit-address-page/{id}')
def render_edit_address_page(id, request : Request, db : Session = Depends(get_db)):
    access_token = request.cookies.get('access_token')

    
    token_data = decode_token(access_token)

    if token_data is None:
        return redirect_to_login()

    if token_data['role'] != 'ROLE_EMPLOYEE':
       return redirect_to_login()

    return templates.TemplateResponse('edit-address.html', {'request' : request, 'address' : AddressExecutor.fetchById(id, token_data['sub'], db), 'user' : UserExecutor.fetchByEmail(token_data['sub'], db)})









# Address API Endpoints

@router.post('', summary= 'Add new Address', dependencies=[Depends(RoleChecker(['ROLE_EMPLOYEE']))])
def create(request : AddAddressRequest,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = AddressExecutor.add(request, tokendetails['sub'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.put('', summary= 'Edit Address', dependencies=[Depends(RoleChecker(['ROLE_EMPLOYEE']))])
def update(request : UpdateAddressRequest,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody =AddressExecutor.update(request, tokendetails['sub'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.get('', summary= 'Get Address by id', dependencies=[Depends(RoleChecker(['ROLE_EMPLOYEE']))])
def getById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = AddressExecutor.getById(id, tokendetails['sub'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.get('/all', summary= 'Get All Address for Employee', dependencies=[Depends(RoleChecker(['ROLE_EMPLOYEE']))])
def getAll(resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody = AddressExecutor.getAll(tokendetails['sub'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.delete('', summary= 'Delete Address by Id', dependencies=[Depends(RoleChecker(['ROLE_EMPLOYEE']))] )
def deleteById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody =AddressExecutor.deleteById(id, tokendetails['sub'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.patch('/primary', summary= 'Set address primary', dependencies=[Depends(RoleChecker(['ROLE_EMPLOYEE']))])
def restoreById(id : int,  resp : Response, db : Session = Depends(get_db), tokendetails: dict = Depends(access_token_bearer)):
    responseBody =AddressExecutor.make_primary(id, tokendetails['sub'], db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)