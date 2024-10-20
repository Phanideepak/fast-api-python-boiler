

class BaseException(Exception):
     status_code = 500
     status_message = 'Internal Error Occurred'
     error_message = status_message

     def __init__(self, status_message = None, status_code = None, errorMessage = None):
          self.status_code = status_code
          self.status_message = status_message

class DataNotFoundException(BaseException):
     def __init__(self, error_message):
          self.error_message = error_message
          super().__init__('Data Not Found Error', 404, error_message)