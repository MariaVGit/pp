from pp24.demo24 import Cat


class Animal:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"jestem zwierzęciem, mam na imię {self.__name}"

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

dog = Dog("Pluto")
print(dog)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

cat = Cat("Tom")
print(cat)
