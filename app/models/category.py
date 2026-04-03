from sqlalchemy import Column, Integer, String, Enum, ForeignKey

from app.core.database import Base
from app.models.transactiontype import TransactionType


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    name = Column(String(100), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)