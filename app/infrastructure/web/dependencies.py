from typing import Iterator

import jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.application.interfaces.repositories import IUserRepository
from app.application.use_cases.user_usecase import UserUseCase
from app.domain.entities.user import User
from app.infrastructure.database.repositories.user_repository import UserRepository
from app.infrastructure.web.auth import oauth2_scheme
from app.utilities.config import settings
from app.utilities.jwt_utils import verify_access_token

# SQLAlchemyエンジンとセッションメーカーの設定
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# データベースセッションの依存性
def get_db_session() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ユーザーリポジトリの依存性
def get_user_repository(db: Session = Depends(get_db_session)) -> IUserRepository:
    return UserRepository(db)


# ユーザーユースケースの依存性
def get_user_use_case(
    repo: IUserRepository = Depends(get_user_repository),
) -> UserUseCase:
    return UserUseCase(repo)


# 現在認証されているユーザーの取得
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_repo: IUserRepository = Depends(get_user_repository),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = verify_access_token(token, credentials_exception)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        user = user_repo.get_by_email(email)
        if user is None:
            raise credentials_exception
        return user
    except jwt.PyJWTError:
        raise credentials_exception
    except Exception as _:
        raise credentials_exception
