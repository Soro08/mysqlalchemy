from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
import bcrypt
from enum import Enum as PythonEnum

Base = declarative_base()

    
class RoleEnum(PythonEnum):
    ADMIN = 'admin'
    STUDENT = 'student'
    CLIENT = 'client'
    
class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    role = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    @validates('role')
    def validate_role(self, key, role):
        if role not in [e.value for e in RoleEnum]:
            raise ValueError(f'Invalid role: {role}')
        return role

    def set_password(self, password):
        # Hachez le mot de passe avec bcrypt avant de le stocker
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        # Vérifiez si le mot de passe correspond au hachage stocké
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

m_c = Base.metadata
