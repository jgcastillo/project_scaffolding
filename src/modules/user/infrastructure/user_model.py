from __future__ import annotations
from sqlmodel import Field
from fastapi_users_db_sqlmodel import SQLModelBaseUserDB

class User(SQLModelBaseUserDB, table=True):
    __tablename__ = "users"
    first_name: str
    last_name: str