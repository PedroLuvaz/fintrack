from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.services.transaction_service import TransactionService

router = APIRouter(prefix="/users/{user_id}/transactions", tags=["transactions"])


@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def create_transaction(user_id: int, data: TransactionCreate, db: Session = Depends(get_db)):
    try:
        service = TransactionService(db)
        return service.create(user_id, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=list[TransactionResponse])
def list_transactions(
    user_id: int,
    start_date: datetime | None = Query(default=None),
    end_date: datetime | None = Query(default=None),
    category_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    service = TransactionService(db)
    return service.list_by_user(user_id, start_date, end_date, category_id)


@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transaction(user_id: int, transaction_id: int, db: Session = Depends(get_db)):
    try:
        service = TransactionService(db)
        service.delete(user_id, transaction_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))