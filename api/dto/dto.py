from typing import List, Optional, TypeVar 
from pydantic import BaseModel, Field

class AddDepartmentBody(BaseModel):
    name : str
    description : str

class ResponseDto(BaseModel):
      statusMessage : str = 'Success'
      status_code : int  = 200 

class ErrorResponse(ResponseDto):
    requestId : Optional[str]  = None 
    exceptionId : Optional[str] = None
    exception : Optional[str] = None

class WrappedResponse(ErrorResponse):
      data : Optional[object] = None
      def _init_(self, data = None, requestId = None, exceptionId = None, exception = None, statusMessage = None, status_code = 0):
          self.data = data
          self.requestId = requestId
          self.exception = exception
          self.exceptionId = exceptionId
          self.statusMessage = statusMessage
          self.status_code = status_code