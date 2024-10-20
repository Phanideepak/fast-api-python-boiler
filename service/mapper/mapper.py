from typing import List
from repository.ems.model.ems import User, Department
from api.dto.dto import UserDto, DepartmentDto

def departmentModelToDepartmentDto(dept : Department):
    return DepartmentDto(id = dept.id, name = dept.name, description=dept.description,
                          approval_status = ('Not Approved','Approved') [dept.is_approved] 
                          ,is_deleted = dept.is_deleted )

def departmentModelToDepartmentDtoList(depts : List):
    deptDtos = []

    for dept in depts:
        deptDtos.append(departmentModelToDepartmentDto(dept))

    return deptDtos

def userModelToUserDto(user : User):
    return UserDto(id = user.id, firstname = user.firstname, lastname = user.lastname, email = user.email, role = user.role.name)

def userModelToUserDtoList(users : List):
    userDtos = []

    for user in users:
        userDtos.append(userModelToUserDto(user))

    return userDtos