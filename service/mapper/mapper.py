from typing import List
from repository.ems.model.ems import Department
from api.dto.dto import DepartmentDto

def departmentModelToDepartmentDto(dept : Department):
    return DepartmentDto(id = dept.id, name = dept.name, description=dept.description,
                          approval_status = ('Not Approved','Approved') [dept.is_approved] 
                          ,is_deleted = dept.is_deleted )

def departmentModelToDepartmentDtoList(depts : List):
    deptDtos = []

    for dept in depts:
        deptDtos.append(departmentModelToDepartmentDto(dept))

    return deptDtos