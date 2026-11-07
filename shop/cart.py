"""Корзина покупателя интернет-магазина."""

from .product import Product


class Cart:
    """Корзина с товарами, выбранными покупателем."""

    def __init__(self, owner):
        self.owner = owner
        self.products = []

    def add(self, product):
        """Добавляет товар в корзину."""
        if not isinstance(product, Product):
            raise TypeError("Only products can be added to the cart")
        self.products.append(product)

    def total(self):
        """Вычисляет стоимость товаров без доставки."""
        return sum(product.price for product in self.products)

    def total_with_delivery(self):
        """Вычисляет общую стоимость с доставкой."""
        return sum(product.price + product.delivery_cost() for product in self.products)

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return f"Корзина пользователя {self.owner.name}: {len(self)} товар(ов)"
