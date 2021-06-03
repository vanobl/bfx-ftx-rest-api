from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/orders", response_model=List[schemas.LogTradesInBase])
def read_lod_trades(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    items = crud.log_trades.get_log_trades(db=db, user_id=current_user.id, skip=skip, limit=limit)
    return items