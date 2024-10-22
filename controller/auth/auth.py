from api.dto.dto import SignUpRequest, LoginRequest
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Response, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from service.executor.auth_executor import AuthExecutor
from config import database
from datetime import timedelta, datetime
from app_secrets.service.dependencies import RefreshTokenBearer
from app_secrets.service.jwt_service import create_access_token

router = APIRouter(prefix= '/auth',tags= ['Auth API'])

get_db = database.get_db

templates = Jinja2Templates(directory='templates')

# Templates
@router.get('/login-page')
def render_login_page(request : Request):
    return templates.TemplateResponse('login.html', {'request' : request})


@router.get('/register-page')
def render_login_page(request : Request):
    return templates.TemplateResponse('register.html', {'request' : request})





# API End Points

@router.post('/signup', summary= 'Signup API')
def signup(request : SignUpRequest,  resp : Response, db : Session = Depends(get_db)):
    responseBody = AuthExecutor.signup(request, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.post('/login', summary= 'Login API')
def login(request : LoginRequest,  resp : Response, db : Session = Depends(get_db)):
    responseBody = AuthExecutor.signin(request, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.post('/refresh_token')
def get_new_access_token(tokendetails : dict = Depends(RefreshTokenBearer())):
    expiry_time_stamp = tokendetails['exp']

    if datetime.fromtimestamp(expiry_time_stamp) > datetime.now():
        new_access_token = create_access_token(tokendetails['sub'], timedelta(days=1), tokendetails['role'])
        return JSONResponse(content={"access_token": new_access_token})
    raise HTTPException('Invalid Token')