from dataclasses import dataclass

from blog.uuid import UUID
from blog.person.name import Name

@dataclass
class User:
    uuid: UUID
    username: str
    name: Name

    def __str__(self) -> str:
        return f"Пользователь {self.username}: {self.name}"