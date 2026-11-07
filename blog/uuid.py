import uuid

from blog.exceptions import InvalidArgumentException


class UUID:
    def __init__(self, value: str) -> None:
        try:
            parse = uuid.UUID(value)
        except (ValueError, TypeError, AttributeError):
            raise InvalidArgumentException(f"Malformed UUID: {value}") from None
        self._value = str(parse)

    @staticmethod
    def random() -> "UUID":
        return UUID(str(uuid.uuid4()))

    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return f"UUID({self._value!r})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, UUID) and self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)
