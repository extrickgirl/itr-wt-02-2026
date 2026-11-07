from os import pread

from app.main.my_class import MyClass as MyClass1
from abc import ABC, abstractmethod

class ParentClass:
    def __init__(self):
        print("Конструктор класса ParentClass")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        print("Конструктор класса ChildClass")

class MyAbstractClass(ABC):
    @abstractmethod
    def get_value(self):
        pass

    def print_value(self):
        print(self.get_value())

class MyChildClass(MyAbstractClass):
    def __init__(self):
        self.c = "c value"

    def __getattr__(self, item):
        def method(*args):
            return f"вызван {item}{args}"

        return method
        # print(f"__getattr__: атрибута {item} нету")
        # return None

    def __setattr__(self, key, value):
        print(f"__setattr__: атрибута {key} равен {value}")

    def get_value(self):
        return "MyChildClass"

obj = MyChildClass()
obj.print_value()
print(obj.get_value1(123,123))


try:
    MyAbstractClass()
except TypeError as error:
    print(f"Нельзя создать абстрактный класс {error}")

if __name__ == "__main__":
    ChildClass()


class CarTemplate(ABC):
    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_name(self):
        ...

class AudiCar(CarTemplate):
    def get_id(self):
        return 1

    def get_name(self):
        return "Audi"

audi = AudiCar()
print(audi.get_id(), audi.get_name())

print(MyClass1())