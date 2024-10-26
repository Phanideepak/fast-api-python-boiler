from api.dto.dto import AddDepartmentBody, UpdateDepartmentBody, WrappedResponse
from sqlalchemy.orm import Session
from app_secrets.service.jwt_service import decode_token
from fastapi import APIRouter, Depends, Response, Request, status
from service.executor.dept_executor import DeptExecutor
from service.executor.user_executor import UserExecutor
from config import database, redis
from app_secrets.service.dependencies import AccessTokenBearer, RoleChecker
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates 
from redis import Redis
from controller.common.common import redirect_to_login

router = APIRouter(prefix= '/user',tags= ['User'])


templates = Jinja2Templates(directory='templates')
get_db = database.get_db
access_token_bearer = AccessTokenBearer()


# Pages
@router.get('/home')
def render_home_page(request : Request, db : Session = Depends(get_db)):
    access_token = request.cookies.get('access_token')

    
    token_data = decode_token(access_token)

    if token_data is None:
        return redirect_to_login()

    if token_data['role'] not in ['ROLE_ADMIN','ROLE_HR']:
       return redirect_to_login()

    return templates.TemplateResponse('home.html', {'request' : request, 'user' : UserExecutor.fetchByEmail(token_data['sub'], db)})




# API End Point

@router.get('/all', summary= 'Get All Users', dependencies=[Depends(RoleChecker(['ROLE_ADMIN']))])
def getAll(resp : Response, db : Session = Depends(get_db), _:dict = Depends(access_token_bearer)):
    responseBody = UserExecutor.getAll(db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)