
def emptyMessage(field):
        return (f"{field} cannot be blank or nill")
    
def noneMessage(field):
    return f"{field} cannot be nill"

def zeroMessage(field):
    return f"{field} cannot be zero"

def isLessThan(field,threshold):
    return f"{field} cannot be less than {threshold}"

def isGreaterThan(field,threshold):
    return f"{field} cannot be greater than {threshold}"

    
class ValidationUtils():
    def isTrue(expression : bool, message : str):
        if not expression:
            raise Exception(message)

    def isEmpty(value : str, field: str):
        if value is None:
           raise Exception(noneMessage(field))
        else:
           value = value.strip()
           if not value:
             raise Exception(emptyMessage(field))  

    
    def isNone(value, field: str):
        if value is None:
            raise Exception(noneMessage(field))
    
    def isZero(value, field: str):
        if value is None:
            raise Exception(noneMessage(field))
        else:
            if value == 0:
                raise Exception(zeroMessage(field))