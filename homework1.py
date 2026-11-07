class BankAccount:
    """Банковский счёт, баланс которого не может быть отрицательным."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        self.balance = self.balance - amount


class Shape:
    """Геометрическая фигура, площадь которой определяется в дочерних классах."""

    def area(self):
        raise NotImplementedError("Метод вычисления площади должен быть реализован в подклассе")


class Circle(Shape):
    """Круг, площадь которого рассчитывается по радиусу."""

    PI = 3.14

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2


class Rectangle(Shape):
    """Прямоугольник, площадь которого равна произведению ширины на высоту."""

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Book:
    """Книга, содержащая название и имя автора."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def description(self):
        return f"{self.title}, автор: {self.author}"


class Library:
    """Библиотека, в которой хранится коллекция книг."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только экземпляры класса Book")
        self._books.append(book)

    def find_by_author(self, author):
        return [book for book in self._books if book.author == author]

    def count(self):
        return len(self._books)



if __name__ == "__main__":
    account = BankAccount("Анна", 100)
    account.deposit(50)
    print("Баланс после пополнения:", account.balance, "руб.")

    try:
        account.withdraw(500)
    except ValueError as error:
        print("Ошибка снятия средств:", error)

    print("Баланс после неудачного снятия:", account.balance, "руб.")

    for shape in (Circle(2), Rectangle(3, 4)):
        print("Площадь фигуры:", shape.area())

    first_library = Library()
    second_library = Library()

    first_library.add_book(Book("Основы Python", "Иван Петров"))
    first_library.add_book(Book("Продвинутый Python", "Иван Петров"))

    print("Количество книг в первой библиотеке:", first_library.count())
    print("Количество книг во второй библиотеке:", second_library.count())

    print("Книги автора Иван Петров:",
          [book.description() for book in first_library.find_by_author("Иван Петров")])

