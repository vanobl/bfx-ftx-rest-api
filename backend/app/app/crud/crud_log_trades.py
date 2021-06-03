from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.log_trades import LogTrades
from app.schemas.log_trades import LogTradesInBase


class CRUDLogTrades(CRUDBase[LogTrades]):
    def get_log_trades(self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100) -> List[LogTrades]:
        return (db.query(self.model).filter(LogTrades.user_id == user_id)).offset(skip).limit(limit).all()


log_trades = CRUDLogTrades(LogTrades)