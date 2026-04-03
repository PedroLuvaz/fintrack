from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.category import CategoryCreate, CategoryResponse
from app.services.category_service import CategoryService

router = APIRouter(prefix="/users/{user_id}/categories", tags=["categories"])


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(user_id: int, data: CategoryCreate, db: Session = Depends(get_db)):
    try:
        service = CategoryService(db)
        return service.create(user_id, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=list[CategoryResponse])
def list_categories(user_id: int, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.list_by_user(user_id)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(user_id: int, category_id: int, db: Session = Depends(get_db)):
    try:
        service = CategoryService(db)
        service.delete(user_id, category_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))