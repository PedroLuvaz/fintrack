from datetime import datetime

from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.repositories.transcation_repository import TransactionRepository
from app.schemas.transaction import TransactionCreate


class TransactionService:
    def __init__(self, db: Session):
        self.repository = TransactionRepository(db)

    def create(self, user_id: int, data: TransactionCreate) -> Transaction:
        transaction = Transaction(
            user_id=user_id,
            category_id=data.category_id,
            amount=data.amount,
            description=data.description,
            type=data.type,
            date=data.date,
        )
        return self.repository.create(transaction)

    def list_by_user(
        self,
        user_id: int,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        category_id: int | None = None,
    ) -> list[Transaction]:
        return self.repository.get_by_user(user_id, start_date, end_date, category_id)

    def delete(self, user_id: int, transaction_id: int) -> None:
        transaction = self.repository.get_by_id(transaction_id)

        if not transaction:
            raise ValueError("Transaction not found")
        if transaction.user_id != user_id:
            raise ValueError("Transaction does not belong to this user")

        self.repository.delete(transaction)