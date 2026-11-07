"""Проверяет получение всех пользователей в двух реализациях."""

import sqlite3

from blog.person.name import Name
from blog.repositories.users.in_memory import InMemoryUsersRepository
from blog.repositories.users.interface import UserRepository
from blog.repositories.users.sqlite import SqliteUsersRepository
from blog.user import User
from blog.uuid import UUID
from init_db import create_schema


def check_get_all(repository: UserRepository) -> None:
    assert repository.get_all() == [], "Пустой репозиторий должен возвращать []"

    first = User(UUID.random(), "ivan", Name("Иван", "Иванов"))
    second = User(UUID.random(), "anna", Name("Анна", "Петрова"))
    repository.save(first)
    repository.save(second)

    users = repository.get_all()
    assert len(users) == 2
    assert {user.username for user in users} == {"ivan", "anna"}

    users.clear()
    assert len(repository.get_all()) == 2, "Изменение списка не должно затрагивать хранилище"

    repository.delete(first.uuid)
    assert len(repository.get_all()) == 1


def main() -> None:
    check_get_all(InMemoryUsersRepository())
    print("Список пользователей в памяти: проверка пройдена")

    with sqlite3.connect(":memory:") as connection:
        create_schema(connection)
        check_get_all(SqliteUsersRepository(connection))
        print("Список пользователей в SQLite: проверка пройдена")


if __name__ == "__main__":
    main()
