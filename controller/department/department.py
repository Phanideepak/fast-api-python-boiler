from api.dto.dto import AddDepartmentBody, WrappedResponse
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Response
from service.executor.dept_executor import DeptExecutor
from config import database
from http import HTTPStatus
router = APIRouter(prefix= '/dept',tags= ['Department'])

get_db = database.get_db

@router.post('', summary= 'Operations related to new data insertion')
def create(request : AddDepartmentBody,  resp : Response, db : Session = Depends(get_db)):
    responseBody = DeptExecutor.add(request, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.put('', summary= 'Operations related to new data insertion')
def create(request : AddDepartmentBody,  resp : Response, db : Session = Depends(get_db)):
    responseBody = DeptExecutor.add(request, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.get('', summary= 'Operations related to Get by Id')
def getById(id : int,  resp : Response, db : Session = Depends(get_db)):
    responseBody = DeptExecutor.getById(id, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.delete('', summary= 'Operations related to Delete by Id')
def getById(id : int,  resp : Response, db : Session = Depends(get_db)):
    responseBody = DeptExecutor.deleteById(id, db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)

@router.get('/all', summary= 'Operations related to Department list')
def getAll(resp : Response, db : Session = Depends(get_db)):
    responseBody = DeptExecutor.getAll(db)
    resp.status_code = responseBody.status_code
    return responseBody.dict(exclude_none= True)