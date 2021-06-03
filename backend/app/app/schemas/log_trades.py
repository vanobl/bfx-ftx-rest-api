import enum
from typing import Optional

from sqlalchemy.sql.sqltypes import Float

from pydantic import BaseModel

class LogTradesBase(BaseModel):
    exchange: Optional[str] = None
    ticker: Optional[str] = None
    order_id: Optional[int] = None
    order_type: Optional[str] = None
    order_status: Optional[str] = None
    order_side: Optional[enum.Enum] = None
    order_size: Optional[Float] = None
    order_price: Optional[Float] = None
    filled_qty: Optional[Float] = None


class LogTradesCreate(LogTradesBase):
    pass


class LogTradesUpdate(LogTradesBase):
    pass

class LogTradesInBase(LogTradesBase):
    id: int
    exchange: str
    user_id: int

    class Config:
        orm_mode = True