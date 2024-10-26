from service.utils.validation_utils import ValidationUtils
from service.utils.response_util import ResponseUtils
from api.dto.dto import AddAddressRequest, UpdateAddressRequest
from service.services.address_service import AddressService
from http import HTTPStatus
from sqlalchemy.orm import Session

class AddressExecutor:

      def add(request : AddAddressRequest, logged_user, db : Session):
            try:
                  ValidationUtils.isEmpty(request.first_line,'first_line')
                  request.first_line = request.first_line.strip()
                  ValidationUtils.isEmpty(request.phone, 'phone')
                  request.phone = request.phone.strip()
                  ValidationUtils.isEmpty(request.city, 'city')
                  request.city = request.city.strip()
                  ValidationUtils.isEmpty(request.pincode, 'pincode')
                  request.pincode = request.pincode.strip()
                  ValidationUtils.isEmpty(request.state, 'state')
                  request.state = request.state.strip()
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e),HTTPStatus.BAD_REQUEST)

            return AddressService.add(request, logged_user, db)
      
      def update(request : UpdateAddressRequest, logged_user, db : Session):
            try:
                  ValidationUtils.isZero(request.id, 'address_id')
                  ValidationUtils.isEmpty(request.first_line,'first_line')
                  request.first_line = request.first_line.strip()
                  ValidationUtils.isEmpty(request.phone, 'phone')
                  request.phone = request.phone.strip()
                  ValidationUtils.isEmpty(request.city, 'city')
                  request.city = request.city.strip()
                  ValidationUtils.isEmpty(request.pincode, 'pincode')
                  request.pincode = request.pincode.strip()
                  ValidationUtils.isEmpty(request.state, 'state')
                  request.state = request.state.strip()
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e),HTTPStatus.BAD_REQUEST)

            return AddressService.update(request, logged_user, db)

      def getById(id, logged_user, db : Session):
            try:
                  ValidationUtils.isZero(id, 'address_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return AddressService.getById(id, logged_user, db)
      
      def fetchById(id, logged_user, db : Session):
            return AddressService.fetchById(id, logged_user, db)

      def getAll(logged_user, db : Session):
            return AddressService.getAll(logged_user, db)
      
      def fetchAll(logged_user, db : Session):
            return AddressService.fetchAll(logged_user, db)
      
      def deleteById(id, logged_user, db : Session):
            try:
                  ValidationUtils.isZero(id, 'dept_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return AddressService.deleteById(id, logged_user, db)
      
      def make_primary(id, logged_user, db : Session):
            try:
                  ValidationUtils.isZero(id, 'dept_id')
            except Exception as e:
                  return ResponseUtils.error_wrap(str(e), HTTPStatus.BAD_REQUEST)
            
            return AddressService.make_primary(id, logged_user, db)