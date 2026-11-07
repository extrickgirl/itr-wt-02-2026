"""Демонстрация замены репозитория без изменения бизнес-логики."""

import sqlite3

from blog.person.name import Name
from blog.repositories.users.in_memory import InMemoryUsersRepository
from blog.repositories.users.interface import UserRepository
from blog.repositories.users.sqlite import SqliteUsersRepository  # noqa: F401
from blog.user import User
from blog.uuid import UUID
from init_db import create_schema


def main() -> None:
    connection = sqlite3.connect(":memory:")
    create_schema(connection)

    users_repository: UserRepository = InMemoryUsersRepository()

    first = User(UUID.random(), "ivan", Name("Ванька", "Ванечкин"))
    second = User(UUID.random(), "anna", Name("Аленка", "Аленечкина"))
    users_repository.save(first)
    users_repository.save(second)

    print(users_repository.get_by_username("vanek"))
    print(users_repository.get_by_username("alenka"))
    connection.close()


if __name__ == "__main__":
    main()
