from blog.exceptions import UserNotFoundException
from blog.repositories.users.interface import UserRepository
from blog.uuid import UUID
from blog.user import User


class InMemoryUsersRepository(UserRepository):
    def __init__(self) -> None:
        self._users: dict[UUID, User] = {}

    def save(self, user: User) -> None:
        self._users[user.uuid] = user

    def get(self, uuid: UUID) -> User:
        if uuid not in self._users:
            raise UserNotFoundException(f"User not found: {uuid}")
        return self._users[uuid]

    def get_by_username(self, username: str) -> User:
        for user in self._users.values():
            if user.username == username:
                return user
        raise UserNotFoundException(f"User not found: {username}")