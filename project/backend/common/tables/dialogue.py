from sqlalchemy import Column, Integer
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship

from common.database import Base
from common.tables.account import Account

class Dialogue(Base):
    __tablename__ = 'dialogues'

    id = Column(Integer, primary_key=True, index=True)
    account1_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    account2_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)

    # Связь с таблицей Account
    account1 = relationship('Account', foreign_keys=[account1_id])
    account2 = relationship('Account', foreign_keys=[account2_id])