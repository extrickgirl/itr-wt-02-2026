"""Проверяет удаление пользователя в двух реализациях репозитория."""

import sqlite3

from blog.exceptions import UserNotFoundException
from blog.person.name import Name
from blog.repositories.users.in_memory import InMemoryUsersRepository
from blog.repositories.users.interface import UserRepository
from blog.repositories.users.sqlite import SqliteUsersRepository
from blog.user import User
from blog.uuid import UUID
from init_db import create_schema


def check_delete(repository: UserRepository) -> None:
    user = User(UUID.random(), "ivan", Name("Иван", "Иванов"))
    repository.save(user)
    assert repository.get(user.uuid) == user

    repository.delete(user.uuid)
    try:
        repository.get(user.uuid)
    except UserNotFoundException:
        pass
    else:
        raise AssertionError("Удалённый пользователь всё ещё доступен")

    try:
        repository.delete(user.uuid)
    except UserNotFoundException:
        pass
    else:
        raise AssertionError("Повторное удаление не вызвало исключение")


def main() -> None:
    check_delete(InMemoryUsersRepository())
    print("Удаление в памяти: проверка пройдена")

    with sqlite3.connect(":memory:") as connection:
        create_schema(connection)
        check_delete(SqliteUsersRepository(connection))
        print("Удаление в SQLite: проверка пройдена")


if __name__ == "__main__":
    main()
