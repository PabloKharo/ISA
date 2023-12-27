from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship

from common.tables.account import Account
from common.database import Base

Base = declarative_base()
class Topic(Base):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    body = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    change_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Связь с таблицей Account
    author = relationship('Account', foreign_keys=[author_id])