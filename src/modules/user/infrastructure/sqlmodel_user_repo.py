from __future__ import annotations
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.modules.user.infrastructure.user_model import User as UserModel
from src.modules.user.domain.user import User as DomainUser
from src.modules.user.domain.repository import IUserRepository


class SQLModelUserRepository(IUserRepository):
    def __init__(self, engine) -> None:
        self.engine = engine

    # ---------- Mappers ----------
    @staticmethod
    def _to_domain(model: UserModel) -> DomainUser:
        return DomainUser(
            id=model.id,
            email=model.email,
            first_name=model.first_name,
            last_name=model.last_name,
        )

    @staticmethod
    def _from_domain(domain: DomainUser) -> UserModel:
        return UserModel(
            id=domain.id,
            email=domain.email,
            first_name=domain.first_name,
            last_name=domain.last_name,
            hashed_password="dummy",
            is_active=True,
        )

    # ---------- Puertos ----------
    async def save(self, user: DomainUser) -> None:
        async with AsyncSession(self.engine) as session:
            session.add(self._from_domain(user))
            await session.commit()

    async def get_by_email(self, email: str) -> DomainUser | None:
        async with AsyncSession(self.engine) as session:
            result = await session.exec(
                select(UserModel).where(UserModel.email == email)
            )
            model = result.first()
            return self._to_domain(model) if model else None
