class Animal:
    all_counter = 0
    def __init__(self, name):
        Animal.all_counter += 1
    def introduce(self):
        print(f"Jestem typem {self.type} mam na imię {self.name}, jest nas {self.counter}", "a wszystkich zwierząt",{self.all_counter},self.make_sound())

class Dog(Animal):
    type = "pies"
    counter = 0

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        Dog.counter += 1

    def make_sound(self):
        return "hau hau"


class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        Cat.counter += 1

    def make_sound(self):
        return "miau"

class Pig(Animal):
    type = "świnka"
    counter = 0
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        Pig.counter += 1

    def make_sound(self):
        return "chrum chrum"

animals = [
    Dog("Jim"),
    Dog("Pluto"),
    Dog("Azor"),
    Dog("Nanu"),
    Cat("Tom"),
    Cat("Julia"),
    Cat("Kitty"),
    Pig("Piggy"),
    Pig("Toby")
]
for animal in animals:
    animal.introduce()
