"""Модель комментария к публикации."""

from dataclasses import dataclass

from blog.person.person import Person
from blog.post import Post


@dataclass
class Comment:
    """Комментарий, связанный с автором и публикацией."""

    author: Person
    post: Post
    text: str

    def __str__(self) -> str:
        return f"{self.author.name} комментирует: {self.text}"
