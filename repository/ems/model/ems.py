from ....config.database import Base
from sqlalchemy import Column, Integer, String, Boolean,DateTime
import datetime

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key = True, autoincrement='auto', index = True)
    name = Column(String, nullable= False)
    description = Column(String, nullable=False)
    is_approved = Column(Boolean, default = True)
    is_deleted = Column(Boolean, default = False)
    created_at = Column(DateTime(), default = datetime.utcnow)
    updated_at = Column(DateTime(), onupdate = datetime.utcnow, default = datetime.utcnow)
