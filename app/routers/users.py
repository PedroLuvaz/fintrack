from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    try:
        service = UserService(db)
        return service.create(data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=UserResponse)
def get_user(
    user_id: int | None = None,
    email: str | None = None,
    db: Session = Depends(get_db)
):
    service = UserService(db)

    try:
        if user_id:
            return service.get_by_id(user_id)
        if email:
            return service.get_by_email(email)

        raise HTTPException(
            status_code=400,
            detail="user_id or email must be provided"
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )