"""Пример создания публикации и комментария к ней."""

from datetime import datetime

from blog.comment import Comment
from blog.person.name import Name
from blog.person.person import Person
from blog.post import Post


def main() -> None:
    """Создаёт публикацию и выводит связанный с ней комментарий."""
    author = Person(
        name=Name(first_name="Ванька", last_name="Ванечкин"),
        registered_on=datetime.now(),
    )
    post = Post(author=author, text="Изучаю dataclass в Python")
    comment = Comment(author=author, post=post, text="Комментирую первым комментарием")

    print(post)
    print(comment)


if __name__ == "__main__":
    main()
