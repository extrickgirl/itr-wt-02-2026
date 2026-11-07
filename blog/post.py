from dataclasses import dataclass

from blog.person.person import Person


@dataclass
class Post:
    author: Person
    text: str

    def __str__(self) -> str:
        return f"{self.author.name} пишет: {self.text}"
