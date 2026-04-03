from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.repositories.base import BaseRepository


class TransactionRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(Transaction, db)

    def get_by_user(
        self,
        user_id: int,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        category_id: int | None = None,
    ):
        stmt = select(Transaction).where(Transaction.user_id == user_id)

        if start_date:
            stmt = stmt.where(Transaction.date >= start_date)
        if end_date:
            stmt = stmt.where(Transaction.date <= end_date)
        if category_id:
            stmt = stmt.where(Transaction.category_id == category_id)

        stmt = stmt.order_by(Transaction.date.desc())
        return list(self.db.scalars(stmt).all())