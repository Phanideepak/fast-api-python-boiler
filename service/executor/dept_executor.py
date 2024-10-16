from service.utils.validation_utils import ValidationUtils
from service.utils.response_util import ResponseUtils
from service.services.dept_service import DeptService
from api.dto.dto import WrappedResponse
from http import HTTPStatus
from sqlalchemy.orm import Session

class DeptExecutor:
      def add(request, db : Session):
            try:
                  ValidationUtils.isEmpty(request.name,'name')
                  ValidationUtils.isEmpty(request.description, 'description')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e),HTTPStatus.BAD_REQUEST)

            return DeptService.add(request, db)
            