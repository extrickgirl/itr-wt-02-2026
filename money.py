"""Денежная сумма с поддержкой сравнения и сложения."""


class Money:
    """Сумма денег с указанной валютой."""

    def __init__(self, amount, currency="RUB"):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"Money(amount={self.amount!r}, currency={self.currency!r})"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot add money in different currencies")
        return Money(self.amount + other.amount, self.currency)


if __name__ == "__main__":
    first = Money(5)
    second = Money(7)
    total = first + second

    print("Строковое представление:", str(first))
    print("Представление для разработчика:", repr(first))
    print("Равные суммы:", "Да" if first == Money(5) else "Нет")
    print("Разные суммы:", "Да" if first == second else "Нет")
    print("Разные валюты равны:", "Да" if first == Money(5, "USD") else "Нет")
    print("Сравнение с числом:", "Да" if first == 5 else "Нет")
    print("Сумма:", total)
    print("Исходные объекты не изменились:", first, "и", second)

    try:
        print(first + Money(5, "USD"))
    except ValueError as error:
        print("Сложение разных валют запрещено:", error)
