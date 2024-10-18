from typing import List, Optional, TypeVar, Generic
from pydantic import BaseModel, Field

T = TypeVar('T')

class AddDepartmentBody(BaseModel):
    name : str
    description : str

class UpdateDepartmentBody(BaseModel):
    id : int = Field(min = 1)
    name : str
    description : str

class DepartmentDto(BaseModel):
     id : int
     name : str
     description : str 
     approval_status : str
     is_deleted : bool
     def __init__(self, id, name, description, approval_status, is_deleted):
          super().__init__(id = id,name = name, description = description, approval_status = approval_status, is_deleted = is_deleted)

class ResponseDto(BaseModel):
      status_message : str = 'Success'
      status_code : int  = 200 

class ErrorResponse(ResponseDto):
    request_id : Optional[str]  = None 
    exception_id : Optional[str] = None
    exception : Optional[str] = None

class WrappedResponse(ErrorResponse):
      data : Optional[T] = None
      def _init_(self, data = None, request_id = None, exception_id = None, exception = None, status_message = None, status_code = 0):
        super().__init__(data = data, requestId = request_id, exceptionId= exception_id, exception=exception, statusMessage = status_message, status_code = status_code)