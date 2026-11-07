import sqlite3

from blog.exceptions import UserNotFoundException
from blog.repositories.users.interface import UserRepository
from blog.user import User
from blog.uuid import UUID
from blog.person.name import Name


class SqliteUsersRepository(UserRepository):
    def __init__(self, connection: sqlite3.Connection) -> None:
        self._connection = connection

    def save(self, user: User) -> None:
        self._connection.execute(
            """
            INSERT INTO users (uuid, username, first_name, last_name)
            VALUES (:uuid, :username, :first_name, :last_name)
            ON CONFLICT (uuid) DO UPDATE SET
            first_name = :first_name,
            last_name = :last_name
            """,
            {
                "uuid": str(user.uuid),
                "username": user.username,
                "first_name": user.name.first_name,
                "last_name": user.name.last_name
            }
        )
        self._connection.commit()

    def get(self, uuid: UUID) -> User:
        cursor = self._connection.execute(
            """
            SELECT uuid, username, first_name, last_name FROM users WHERE uuid = :uuid
            """,
            {
                "uuid": str(uuid)
            }
        )
        return self._fetch_user(cursor, str(uuid))

    def get_by_username(self, username: str) -> User:
        cursor = self._connection.execute(
            """
            SELECT uuid, username, first_name, last_name FROM users WHERE username = :username
            """,
            {
                "username": username
            }
        )
        return self._fetch_user(cursor, username)

    def _fetch_user(self, cursor: sqlite3.Cursor, payload: str) -> User:
        row = cursor.fetchone()
        if row is None:
            raise UserNotFoundException(f"User not found: {payload}")
        uuid, username, first_name, last_name = row
        return User(UUID(uuid), username, Name(first_name, last_name))