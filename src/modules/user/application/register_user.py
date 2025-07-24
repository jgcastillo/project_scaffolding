from dataclasses import dataclass
from uuid import UUID

from modules.user.domain.user import User
from modules.user.domain.repository import IUserRepository

@dataclass(slots=True)
class RegisterUserCommand:
    user_id: UUID
    email: str
    first_name: str
    last_name: str

class RegisterUserHandler:
    def __init__(self, repo: IUserRepository) -> None:
        self._repo = repo

    async def handle(self, cmd: RegisterUserCommand) -> None:
        user = User(
            id=cmd.user_id,
            email=cmd.email,
            first_name=cmd.first_name,
            last_name=cmd.last_name,
        )
        await self._repo.save(user)