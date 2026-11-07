print("hi")

class Article:
    def __init__(self):
        self._id = None
        self._title = "Заголовок"
        self._content = "Текст статьи"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def view(self):
        print(f"<h1>{self._title}</h1><p>{self._content}</p>")

article1 = Article()
article2 = Article()

article2.id = 1
article1.id = 2

print(article2.id)
print(article1.id)

class Animal:
    def breath(self):
        print("breath 1")

class Mammal(Animal):
    def __init__(self):
        self._tail = True

class Cat(Mammal):
    def mew(self):
        print("mew")

    def breath(self):
        print("breath 2")

class Dog(Mammal):
    def woof(self):
        print("woof")

for animal in (Cat(), Dog()):
    animal.breath()


class Wheels:
    def run(self):
        print("Колеса крутятся")

class Engine:
    pass

class Car:
    def __init__(self, model):
        self._model = model
        self._engine = Engine()
        self._wheels = Wheels()

    @property
    def wheels(self):
        return self._wheels

car = Car("x5")
car.wheels.run()

class MathOperation:
    PI = 3.14

    @staticmethod
    def circle_length(radius):
        return 2 * radius * MathOperation.PI

class Logger:
    WARNING = 1
    INFO = 2
    ERROR = 3

print(Logger.ERROR)