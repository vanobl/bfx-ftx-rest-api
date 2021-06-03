import enum
from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float, TIMESTAMP
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Sides(enum.Enum):
    buy = 1
    sell = 2


class LogTrades(Base):
    id = Column(Integer, primary_key=True, index=True)
    exchange = Column(String(256))
    ticker = Column(String(256))
    order_id = Column(Integer)
    order_type = Column(String(256))
    order_status = Column(String(256))
    order_side = Column(Enum(Sides))
    order_size = Column(Float(precision=10, asdecimal=2))
    order_price = Column(Float(precision=10, asdecimal=2))
    filled_qty = Column(Float(precision=10, asdecimal=2))
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)
    user_id = relationship("User", back_populates="log_trades")