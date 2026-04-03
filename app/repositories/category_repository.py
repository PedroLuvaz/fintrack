from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.category import Category
from app.repositories.base import BaseRepository


class CategoryRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(Category, db)

    def get_by_user(self, user_id: int):
        stmt = select(Category).where(Category.user_id == user_id)
        return list(self.db.scalars(stmt).all())