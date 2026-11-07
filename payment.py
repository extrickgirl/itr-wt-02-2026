"""Способы оплаты с использованием абстрактного класса."""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """Общий интерфейс для способов оплаты."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def pay(self, amount):
        """Выполняет оплату указанной суммы."""

    def describe(self):
        """Выводит название способа оплаты."""
        print(f"Способ оплаты: {self.name}")


class CardPayment(PaymentMethod):
    """Оплата банковской картой с указанием последних цифр."""

    def __init__(self, last_digits):
        super().__init__("Банковская карта")
        self.last_digits = str(last_digits)

    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
        return f"Картой **** {self.last_digits} оплачено {amount} руб."


class CashPayment(PaymentMethod):
    """Оплата наличными при получении заказа."""

    def __init__(self):
        super().__init__("Наличные")

    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
        return f"Наличными оплачено {amount} руб."


if __name__ == "__main__":
    try:
        PaymentMethod("Любой способ")
    except TypeError:
        print("Нельзя создать объект абстрактного класса PaymentMethod")

    for method in (CardPayment("1234"), CashPayment()):
        method.describe()
        print(method.pay(100))

    class IncompletePayment(PaymentMethod):
        """Неполный способ оплаты без реализации pay."""

        def __init__(self):
            super().__init__("Неполный способ")

    try:
        IncompletePayment()
    except TypeError:
        print("Нельзя создать способ оплаты без метода pay")
