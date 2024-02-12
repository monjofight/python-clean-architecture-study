from logging import getLogger
from typing import Optional

from app.application.interfaces.repositories import IUserRepository
from app.domain.entities.user import User
from app.utilities.jwt_utils import create_access_token
from app.utilities.password_utils import hash_password, verify_password

# ロガーの設定
logger = getLogger(__name__)


class UserUseCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def create_user(self, name: str, email: str, password: str) -> User:
        # パスワードをハッシュ化してユーザーを作成
        hashed_password = hash_password(password)
        user = User(name=name, email=email, hashed_password=hashed_password)
        return self.user_repository.add(user)

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        # メールでユーザーを検索
        user = self.user_repository.get_by_email(email)
        if user and verify_password(password, user.hashed_password):
            # パスワードが一致した場合、ユーザーを返す
            return user
        else:

            # 認証に失敗した場合、Noneを返す
            return None

    def generate_access_token(self, user: User) -> str:
        # JWTアクセストークンを生成
        token_data = {"sub": user.email}
        return create_access_token(data=token_data)

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        # IDによるユーザー情報の取得
        return self.user_repository.get_user(user_id)

    def update_user(
        self,
        user_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
    ) -> Optional[User]:
        # パスワードが提供された場合、ハッシュ化する
        hashed_password = hash_password(password) if password else None
        # ユーザー情報の更新
        return self.user_repository.update(user_id, name, email, hashed_password)

    def delete_user(self, user_id: int) -> bool:
        # ユーザーの削除
        return self.user_repository.delete(user_id)
