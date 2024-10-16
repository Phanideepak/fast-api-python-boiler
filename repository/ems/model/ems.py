from config.database import Base
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Boolean,DateTime
from datetime import datetime

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key = True, autoincrement='auto', index = True)
    name = Column(String, nullable= False)
    description = Column(String, nullable=False)
    is_approved = Column(Boolean, default = True)
    is_deleted = Column(Boolean, default = False)
    created_at = Column(DateTime(), default = datetime.now())
    updated_at = Column(DateTime(), onupdate = datetime.now(), default = datetime.now())

    def __init__(self, name, description):
        self.name = name 
        self.description = description
