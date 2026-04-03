from datetime import datetime

from sqlalchemy.orm import Session

from app.core.transactiontype import TransactionType
from app.repositories.transcation_repository import TransactionRepository


class SummaryService:
    def __init__(self, db: Session):
        self.repository = TransactionRepository(db)

    def get_summary(
        self,
        user_id: int,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
    ) -> dict:
        transactions = self.repository.get_by_user(user_id, start_date, end_date)

        total_income = sum(t.amount for t in transactions if t.type == TransactionType.INCOME)
        total_expense = sum(t.amount for t in transactions if t.type == TransactionType.EXPENSE)

        expense_by_category: dict[str, float] = {}
        for t in transactions:
            if t.type == TransactionType.EXPENSE:
                name = t.category.name if t.category else "Sem categoria"
                expense_by_category[name] = expense_by_category.get(name, 0) + t.amount

        return {
            "total_income": round(total_income, 2),
            "total_expense": round(total_expense, 2),
            "balance": round(total_income - total_expense, 2),
            "expense_by_category": expense_by_category,
        }