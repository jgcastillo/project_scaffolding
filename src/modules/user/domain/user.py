from __future__ import annotations
from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class User:
    id: UUID
    email: str
    first_name: str
    last_name: str
