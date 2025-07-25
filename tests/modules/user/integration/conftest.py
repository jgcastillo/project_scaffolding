from __future__ import annotations
import pytest
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

from src.modules.user.application.register_user import RegisterUserHandler
from src.modules.user.infrastructure.sqlmodel_user_repo import SQLModelUserRepository


@pytest.fixture(scope="function")
async def async_engine():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield engine
    await engine.dispose()


@pytest.fixture(scope="function")
async def repo(async_engine):
    return SQLModelUserRepository(engine=async_engine)


@pytest.fixture(scope="function")
async def handler(repo):
    return RegisterUserHandler(repo)
