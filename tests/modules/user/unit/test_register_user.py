from uuid import uuid4

from modules.user.application.register_user import (
    RegisterUserCommand,
    RegisterUserHandler,
)
from tests.modules.user.unit.fake_user_repo import FakeUserRepository


async def test_register_user_success():
    # Arrange
    repo = FakeUserRepository()
    handler = RegisterUserHandler(repo)

    cmd = RegisterUserCommand(
        user_id=uuid4(),
        email="john.doe@example.com",
        first_name="John",
        last_name="Doe",
    )

    # Act
    await handler.handle(cmd)

    # Assert
    user = await repo.get_by_email("john.doe@example.com")
    assert user is not None
    assert user.email == "john.doe@example.com"
    assert user.first_name == "John"
    assert user.last_name == "Doe"
