from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.adapters.requests.user_request import UserCreateRequest
from app.adapters.responses.user_response import UserResponse
from app.application.use_cases.user_usecase import UserUseCase
from app.domain.entities.user import User
from app.infrastructure.web.auth import oauth2_scheme  # noqa
from app.infrastructure.web.dependencies import (
    get_current_user,
    get_user_use_case,
)

router = APIRouter()


@router.post("/signup/", status_code=status.HTTP_201_CREATED)
def signup(
    user_request: UserCreateRequest = Body(...),
    user_use_case: UserUseCase = Depends(get_user_use_case),
):
    created_user = user_use_case.create_user(
        name=user_request.name,
        email=user_request.email,
        password=user_request.password,
    )
    return {"message": "User created successfully", "user_id": created_user.id}


@router.post("/login/")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_use_case: UserUseCase = Depends(get_user_use_case),
):
    user = user_use_case.authenticate_user(
        email=form_data.username,
        password=form_data.password,
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = user_use_case.generate_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me/", response_model=UserResponse)
def read_users_me(
    current_user: User = Depends(get_current_user),
):
    # レスポンスモデルに変換
    return UserResponse(
        id=current_user.id, name=current_user.name, email=current_user.email
    )
