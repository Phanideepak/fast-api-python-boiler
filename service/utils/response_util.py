from api.dto.dto import WrappedResponse
import secrets

class ResponseUtils:
    def wrap(data):
        return WrappedResponse(data)
    
    def wrap():
        return WrappedResponse()
    
    def error_wrap(error_message, code):
        resp = WrappedResponse()
        resp.statusMessage = 'Error Occured'
        resp.status_code = code
        resp.exception = error_message
        resp.exceptionId = secrets.token_hex(16)
        return resp