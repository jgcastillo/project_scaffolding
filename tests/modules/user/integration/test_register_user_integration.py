import pytest
from uuid import uuid4
from src.modules.user.application.register_user import RegisterUserCommand


@pytest.mark.asyncio
async def test_register_user_with_real_repo(handler, repo):
    cmd = RegisterUserCommand(
        user_id=uuid4(),
        email="alice@example.com",
        first_name="Alice",
        last_name="Wonder",
    )

    await handler.handle(cmd)
    user = await repo.get_by_email("alice@example.com")
    assert user is not None
    assert user.email == "alice@example.com"
