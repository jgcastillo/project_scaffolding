from abc import ABC, abstractmethod
from .user import User


class IUserRepository(ABC):

    @abstractmethod
    async def save(self, user: User) -> None: ...

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None: ...
