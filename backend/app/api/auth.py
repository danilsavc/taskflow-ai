from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.core.config import settings
from app.core.database import get_db
from app.core.security import create_access_token
from app.models.user import User
from app.schemas.user import UserLogin, UserRegister
from app.services.auth_service import (
    EmailAlreadyRegisteredError,
    InvalidCredentialsError,
    authenticate_user,
    register_user,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user_endpoint(
    user_data: UserRegister, db: AsyncSession = Depends(get_db)
):
    try:
        new_user = await register_user(
            db=db,
            email=user_data.email,
            password=user_data.password,
        )
    except EmailAlreadyRegisteredError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    return {
        "id": new_user.id,
        "email": new_user.email,
        "created_at": new_user.created_at,
    }


@router.post("/login")
async def login_user_endpoint(
    user_data: UserLogin, response: Response, db: AsyncSession = Depends(get_db)
):
    try:
        user = await authenticate_user(
            db=db, email=user_data.email, password=user_data.password
        )
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
        )

    access_token = create_access_token(user.id)

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=settings.access_token_expire_minutes * 60,
        path="/",
    )

    return {
        "message": "Login successful",
        "user_id": user.id,
        "email": user.email,
    }


@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "created_at": current_user.created_at,
    }


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie(
        key="access_token", httponly=True, secure=False, samesite="lax", path="/"
    )

    return {"message": "Logout successful"}
