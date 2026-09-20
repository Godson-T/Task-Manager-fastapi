from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)