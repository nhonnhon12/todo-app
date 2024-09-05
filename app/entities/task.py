import enum
from sqlalchemy import Column, String, Enum, SmallInteger, ForeignKey, Uuid
from database import Base
from entities.base_entity import BaseEntity
from passlib.context import CryptContext
from sqlalchemy.orm import relationship

bcrypt_context = CryptContext(schemes=["bcrypt"])

class TaskStatus(enum.Enum):
    NEW = 'NEW'
    ACTIVE = 'ACTIVE'
    DONE = 'DONE'

class Task(BaseEntity, Base):
    __tablename__ = "tasks"

    summary = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.NEW)
    priority = Column(SmallInteger)
    user_id = Column(Uuid, ForeignKey("users.id"), nullable=False)

    assignee = relationship("User", back_populates="tasks")
