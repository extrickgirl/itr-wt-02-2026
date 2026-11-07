"""Пример работы интернет-магазина из пакета shop."""

from shop import (
    Cart,
    DigitalProduct,
    FeedbackForm,
    HeavyProduct,
    Product,
    RegularProduct,
    Review,
    User as Customer,
)


if __name__ == "__main__":
    try:
        Product("Товар", 100)
    except TypeError:
        print("Нельзя создать абстрактный класс Product")

    user = Customer("Анна", "anna@example.com")
    book = RegularProduct("Книга по Python", 1000)
    course = DigitalProduct("Курс по Python", 2500)
    fridge = HeavyProduct("Холодильник", 30000, 40)

    cart = Cart(user)
    for product in (book, course, fridge):
        cart.add(product)
        print(f"{product.name}: стоимость доставки = {product.delivery_cost()} руб.")

    print("Покупатель:", user.contact())
    print("Корзина:", cart)
    print("Количество товаров:", len(cart))
    print("Стоимость товаров:", cart.total(), "руб.")
    print("Стоимость с доставкой:", cart.total_with_delivery(), "руб.")

    review = Review(user, book, 5, "Очень полезная книга!")
    book.add_review(review)
    print("Отзыв положительный:", "Да" if review.is_positive() else "Нет")
    print("Количество отзывов на книгу:", len(book.reviews))

    feedback = FeedbackForm(user, "Пожалуйста, свяжитесь со мной")
    print(feedback.send())
