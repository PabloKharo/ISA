from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum

from common.database import Base

class GenderEnum(str, Enum):
    Male = 'Male'
    Female = 'Female'

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    sex = Column(SQLAlchemyEnum(GenderEnum), nullable=False)

class AccountCreate(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str
    email: str
    sex: GenderEnum

class AccountOut(BaseModel):
    login: str
    first_name: str
    last_name: str
    email: str
    sex: GenderEnum