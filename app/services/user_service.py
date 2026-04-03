from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create(self, data: UserCreate) -> User:
        existing = self.repository.get_by_email(data.email)
        if existing:
            raise ValueError("Email already registered")

        user = User(name=data.name, email=data.email)
        return self.repository.create(user)

    def get_by_id(self, user_id: int) -> User:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user
    
    def get_by_email(self, user_email: str) -> User:
        user = self.repository.get_by_email(user_email)
        if not user:
            raise ValueError("User not found")
        return user