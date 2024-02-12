from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> User:
        """
        新しいユーザーをリポジトリに追加します。

        :param user: User エンティティ
        :return: リポジトリに追加された User エンティティ
        """
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        """
        指定されたIDのユーザーを取得します。

        :param user_id: ユーザーのID
        :return: 該当するユーザーのエンティティ、存在しない場合は None
        """
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """
        指定されたメールアドレスのユーザーを取得します。

        :param email: ユーザーのメールアドレス
        :return: 該当するユーザーのエンティティ、存在しない場合は None
        """
        pass

    @abstractmethod
    def update(
        self,
        user_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        hashed_password: Optional[str] = None,
    ) -> Optional[User]:
        """
        指定されたIDのユーザー情報を更新します。

        :param user_id: ユーザーのID
        :param name: 更新するユーザーの名前（省略可能）
        :param email: 更新するユーザーのメールアドレス（省略可能）
        :param hashed_password: 更新するユーザーのハッシュ化されたパスワード（省略可能）
        :return: 更新されたユーザーのエンティティ、存在しない場合は None
        """
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        """
        指定されたIDのユーザーを削除します。

        :param user_id: ユーザーのID
        :return: 削除が成功した場合は True、そうでない場合は False
        """
        pass
