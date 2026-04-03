from datetime import datetime

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.summary_service import SummaryService

router = APIRouter(prefix="/users/{user_id}/summary", tags=["summary"])


@router.get("/")
def get_summary(
    user_id: int,
    start_date: datetime | None = Query(default=None),
    end_date: datetime | None = Query(default=None),
    db: Session = Depends(get_db),
):
    service = SummaryService(db)
    return service.get_summary(user_id, start_date, end_date)