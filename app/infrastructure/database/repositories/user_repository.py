from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.application.interfaces.repositories import IUserRepository
from app.domain.entities.user import User as DomainUser
from app.infrastructure.database.models.user_model import UserModel
from app.utilities.password_utils import hash_password


class UserRepository(IUserRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, user: DomainUser) -> DomainUser:
        new_user = UserModel(
            name=user.name, email=user.email, hashed_password=user.hashed_password
        )
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
        return DomainUser(
            id=new_user.id,
            name=new_user.name,
            email=new_user.email,
            hashed_password=new_user.hashed_password,
        )

    def get_user(self, user_id: int) -> DomainUser:
        user_model = (
            self.db_session.query(UserModel).filter(UserModel.id == user_id).first()
        )
        if user_model is None:
            return None
        return DomainUser(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email,
            hashed_password=user_model.hashed_password,
        )

    def get_by_email(self, email: str) -> DomainUser:
        try:
            user_model = (
                self.db_session.query(UserModel).filter(UserModel.email == email).one()
            )
            return DomainUser(
                id=user_model.id,
                name=user_model.name,
                email=user_model.email,
                hashed_password=user_model.hashed_password,
            )
        except NoResultFound:
            return None

    def update(
        self,
        user_id: int,
        name: str = None,
        email: str = None,
        hashed_password: str = None,
    ) -> DomainUser:
        user_model = (
            self.db_session.query(UserModel).filter(UserModel.id == user_id).first()
        )
        if user_model is None:
            return None
        if name:
            user_model.name = name
        if email:
            user_model.email = email
        if hashed_password:
            user_model.hashed_password = hash_password(hashed_password)
        self.db_session.commit()
        return DomainUser(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email,
            hashed_password=user_model.hashed_password,
        )

    def delete(self, user_id: int) -> bool:
        try:
            user_model = (
                self.db_session.query(UserModel).filter(UserModel.id == user_id).one()
            )
            self.db_session.delete(user_model)
            self.db_session.commit()
            return True
        except NoResultFound:
            return False
