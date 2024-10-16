from api.dto.dto import AddDepartmentBody, WrappedResponse
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Response
from service.executor.dept_executor import DeptExecutor
from config import database
from http import HTTPStatus
router = APIRouter(prefix= '/dept',tags= ['Department'])

get_db = database.get_db

@router.post('/')
def create(request : AddDepartmentBody,  resp : Response, db : Session = Depends(get_db)):
    responseBody = DeptExecutor.add(request, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)