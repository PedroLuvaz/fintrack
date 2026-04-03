from sqlalchemy import select
from sqlalchemy.orm import session

class BaseRepository:
    def __init__(self, model, db: session):
        self.model = model
        self.db = db
    
    def get_by_id(self, id: int):
        return self.db.get(self.model, id)
    
    def get_all(self, skip: int = 0, limit: int = 100):
        stmt = select(self.model).offset(skip).limit(limit)
        return list(self.db.scalas(stmt).all())

    def create(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def delete(self, obj) -> None:
        self.db.delete(obj)
        self.db.commit()

