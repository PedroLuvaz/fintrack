from datetime import datetime
from pydantic import BaseModel, field_validator
from app.core.transactiontype import TransactionType
from app.core.validators import validate_positive_amount


class TransactionCreate(BaseModel):
    category_id: int
    amount: float
    description: str | None = None
    type: TransactionType
    date: datetime

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, v: float) -> float:
        return validate_positive_amount(v)


class TransactionResponse(BaseModel):
    model_config = {"from_attributes": True}

    id: int
    user_id: int
    category_id: int
    amount: float
    description: str | None
    type: TransactionType
    date: datetime
    created_at: datetime