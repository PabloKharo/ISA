from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum
from datetime import datetime
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship

from common.tables.account import Account
from common.tables.dialogue import Dialogue
from common.database import Base

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    dialogue_id = Column(Integer, ForeignKey('dialogues.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    body = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

    # Связь с таблицей Dialogue
    dialogue = relationship('Dialogue', backref='messages')
    author = relationship('Account', foreign_keys=[author_id])