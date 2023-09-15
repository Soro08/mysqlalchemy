from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

from enum import Enum as PythonEnum

Base = declarative_base()

    
class RoleEnum(PythonEnum):
    ADMIN = 'admin'
    STUDENT = 'student'
    CLIENT = 'client'
    
class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    namenom = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    role = Column(String, nullable=False)
    
    @validates('role')
    def validate_role(self, key, role):
        if role not in [e.value for e in RoleEnum]:
            raise ValueError(f'Invalid role: {role}')
        return role


m_c = Base.metadata
