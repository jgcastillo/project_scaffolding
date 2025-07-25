from typing import Dict
from modules.user.domain.repository import IUserRepository
from modules.user.domain.user import User


class FakeUserRepository(IUserRepository):
    def __init__(self) -> None:
        self._store: Dict[str, User] = {}

    async def save(self, user: User) -> None:
        self._store[str(user.email)] = user

    async def get_by_email(self, email: str) -> User | None:
        return self._store.get(email)
