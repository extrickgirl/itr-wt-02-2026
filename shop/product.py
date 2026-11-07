"""Товары интернет-магазина и их способы доставки."""

from abc import ABC, abstractmethod


class Product(ABC):
    """Абстрактный товар с ценой и отзывами."""

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.reviews = []

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero")
        self._price = value

    @abstractmethod
    def delivery_cost(self):
        """Возвращает стоимость доставки товара."""

    def add_review(self, review):
        """Добавляет отзыв, относящийся к этому товару."""
        from .review import Review

        if not isinstance(review, Review):
            raise TypeError("Review must be a Review instance")
        if review.product is not self:
            raise ValueError("Review belongs to a different product")
        self.reviews.append(review)


class RegularProduct(Product):
    """Обычный товар отличается фиксированной стоимостью доставки."""

    def __init__(self, name, price):
        super().__init__(name, price)

    def delivery_cost(self):
        return 300


class DigitalProduct(Product):
    """Цифровой товар отличается отсутствием стоимости доставки."""

    def __init__(self, name, price):
        super().__init__(name, price)

    def delivery_cost(self):
        return 0


class HeavyProduct(Product):
    """Тяжёлый товар отличается расчётом доставки по весу."""

    def __init__(self, name, price, weight):
        super().__init__(name, price)
        if weight <= 0:
            raise ValueError("Weight must be greater than zero")
        self.weight = weight

    def delivery_cost(self):
        return 300 + self.weight * 50
