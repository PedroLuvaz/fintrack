from sqlalchemy.orm import Session

from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate


class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def create(self, user_id: int, data: CategoryCreate) -> Category:
        category = Category(
            user_id=user_id,
            name=data.name,
            type=data.type,
        )
        return self.repository.create(category)

    def list_by_user(self, user_id: int) -> list[Category]:
        return self.repository.get_by_user(user_id)

    def delete(self, user_id: int, category_id: int) -> None:
        category = self.repository.get_by_id(category_id)

        if not category:
            raise ValueError("Category not found")
        if category.user_id != user_id:
            raise ValueError("Category does not belong to this user")

        self.repository.delete(category)