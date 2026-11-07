from dataclasses import dataclass
from datetime import datetime

from blog.person.name import Name


@dataclass
class Person:
    name: Name
    registered_on: datetime

    def __str__(self) -> str:
        return f"{self.name} (на сайте с {self.registered_on:%Y-%m-%d})"
