"""Примеры объектно-ориентированного программирования для интернет-магазина."""


class Product:
    """Товар, который можно приобрести в интернет-магазине."""

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
            raise ValueError("Цена должна быть больше нуля")
        self._price = value

    def delivery_cost(self):
        return 300

    def add_review(self, review):
        if not isinstance(review, Review):
            raise TypeError("Отзыв должен быть экземпляром класса Review")
        if review.product is not self:
            raise ValueError("Отзыв относится к другому товару")
        self.reviews.append(review)


class DigitalProduct(Product):
    """Цифровой товар отличается от обычного бесплатной доставкой."""

    def delivery_cost(self):
        return 0


class HeavyProduct(Product):
    """Доставка тяжёлого товара рассчитывается в зависимости от его веса."""

    def __init__(self, name, price, weight):
        super().__init__(name, price)
        if weight <= 0:
            raise ValueError("Вес должен быть больше нуля")
        self.weight = weight

    def delivery_cost(self):
        return 300 + self.weight * 50


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
            raise ValueError("Адрес электронной почты должен содержать символ @")
        self._email = value

    def contact(self):
        return f"{self.name}: {self.email}"


class Review:
    """Оценка и комментарий покупателя о товаре."""

    def __init__(self, author, product, rating, comment):
        self.author = author
        self.product = product
        self.rating = rating
        self.comment = comment

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or not 1 <= value <= 5:
            raise ValueError("Оценка должна быть от 1 до 5")
        self._rating = value

    def is_positive(self):
        return self.rating >= 4


class Cart:
    """Корзина, в которой хранятся товары, выбранные покупателем."""

    def __init__(self, owner):
        self.owner = owner
        self.products = []

    def add(self, product):
        if not isinstance(product, Product):
            raise TypeError("В корзину можно добавлять только товары")
        self.products.append(product)

    def total(self):
        return sum(product.price for product in self.products)

    def total_with_delivery(self):
        return sum(product.price + product.delivery_cost() for product in self.products)


class FeedbackForm:
    """Форма для хранения сообщения, отправленного покупателем."""

    def __init__(self, user, message):
        self.user = user
        self.message = message
        self.sent = False

    def send(self):
        if not self.message.strip():
            raise ValueError("Сообщение не может быть пустым")
        self.sent = True
        return f"Сообщение от пользователя {self.user.name} отправлено"



if __name__ == "__main__":
    user = User("Анна", "anna@example.com")
    book = Product("Книга по Python", 1000)
    course = DigitalProduct("Курс по Python", 2500)
    fridge = HeavyProduct("Холодильник", 30000, 40)

    cart = Cart(user)
    for product in (book, course, fridge):
        cart.add(product)
        print(f"{product.name}: стоимость доставки = {product.delivery_cost()} руб.")

    print("Покупатель:", user.contact())
    print("Общая стоимость товаров:", cart.total(), "руб.")
    print("Стоимость с учётом доставки:", cart.total_with_delivery(), "руб.")

    review = Review(user, book, 5, "Очень полезная книга!")
    book.add_review(review)
    print("Отзыв положительный:", "Да" if review.is_positive() else "Нет")
    print("Количество отзывов на книгу:", len(book.reviews))

    feedback = FeedbackForm(user, "Пожалуйста, свяжитесь со мной")
    print(feedback.send())
