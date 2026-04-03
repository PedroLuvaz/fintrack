from pydantic import BaseModel
from app.core.transactiontype import TransactionType


class CategoryCreate(BaseModel):
    name: str
    type: TransactionType


class CategoryResponse(BaseModel):
    model_config = {"from_attributes": True}

    id: int
    user_id: int
    name: str
    type: TransactionType