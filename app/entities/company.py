import enum
from database import Base
from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from entities.base_entity import BaseEntity
from entities.user import User

class CompanyMode(enum.Enum):
    MODE_1 = 'MODE 1'
    MODE_2 = 'MODE 2'

class Company(BaseEntity, Base):
    __tablename__ = "companies"

    name = Column(String)
    description = Column(String)
    mode = Column(Enum(CompanyMode), nullable=False, default=CompanyMode.MODE_1)
    
    users = relationship(User, back_populates="company")
