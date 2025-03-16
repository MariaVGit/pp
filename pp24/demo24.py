class Animal:
    pass
class Dog(Animal):
    pass
class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))

print(isinstance(dog, Dog))
print(isinstance(cat, Animal))

