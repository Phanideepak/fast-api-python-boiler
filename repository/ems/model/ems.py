from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean,DateTime, Enum as sqlEnum
from enum import Enum
from datetime import datetime

class Role(Enum):
      ROLE_ADMIN = 'ROLE_ADMIN'
      ROLE_HR = 'ROLE_HR'
      ROLE_FINANCE = 'ROLE_FINANCE'
      ROLE_EMPLOYEE = 'ROLE_EMPLOYEE'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key= True, autoincrement= 'auto', index = True)
    firstname = Column(String, nullable = False)
    lastname = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    role = Column(sqlEnum(Role), default = Role.ROLE_ADMIN, nullable = False)
    created_at = Column(DateTime(), default = datetime.now())
    updated_at = Column(DateTime(), onupdate = datetime.now(), default = datetime.now())

    def __init__(self, email, firstname, lastname, password, role, id = None):
        self.id = id
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.role = role 
         

  

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key = True, autoincrement='auto', index = True)
    name = Column(String, nullable= False)
    description = Column(String, nullable=False)
    is_approved = Column(Boolean, default = False)
    approved_by = Column(Integer)
    approved_at = Column(DateTime())
    deleted_by = Column(Integer)
    deleted_at = Column(DateTime())
    created_by = Column(Integer, nullable = False)
    is_deleted = Column(Boolean, default = False)
    created_at = Column(DateTime(), default = datetime.now())
    updated_at = Column(DateTime(), onupdate = datetime.now(), default = datetime.now())

    def __init__(self, name = None, description = None, created_by = None, id = None):
        self.id = id
        self.name = name 
        self.description = description
        self.created_by = created_by
