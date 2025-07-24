import os
from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
from sqlmodel import SQLModel
from src.core.infrastructure.settings import settings

# Cargar modelo para registrar tabla
from src.modules.user.infrastructure.user_model import User  # noqa: F401

fileConfig(context.config.config_file_name)

sync_url = str(settings.database_sync_url)
context.config.set_main_option("sqlalchemy.url", sync_url)

target_metadata = SQLModel.metadata

def run_migrations_online():
    connectable = create_engine(sync_url, pool_pre_ping=True)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()