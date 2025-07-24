from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # driver asincrono para la base de datos
    database_url: PostgresDsn

    # driver sincrono para la base de datos
    database_sync_url: PostgresDsn

settings = Settings()