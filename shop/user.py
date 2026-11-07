"""Покупатели интернет-магазина."""


class User:
    """Покупатель с именем и адресом электронной почты."""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Email must contain @")
        self._email = value

    def contact(self):
        """Возвращает контактные данные покупателя."""
        return f"{self.name}: {self.email}"
