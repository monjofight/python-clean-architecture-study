from typing import Optional


class User:
    def __init__(
        self,
        name: str,
        email: str,
        hashed_password: str,
        id: Optional[int] = None,
    ):
        self.id = id
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
