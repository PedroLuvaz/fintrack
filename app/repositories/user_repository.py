from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_email(self, email: str):
        stmt = select(User).where(User.email == email)
        return self.db.scalars(stmt).first()