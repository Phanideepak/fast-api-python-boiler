from api.dto.dto import WrappedResponse
import secrets

class ResponseUtils:
    def wrap(data = None):
        return WrappedResponse(data = data)
    
    def error_wrap(error_message, code):
        return WrappedResponse(status_message = 'Error Occured',  status_code= code, exception=error_message, exception_id= secrets.token_hex(16))