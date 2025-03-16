class Person:
    def __init__(self, name,age):
        self.__name = name
        self.__age = age

    def introduce(self):
        print("Jestem " + self.__name, " i mam ", self.__age, " lat")

persons = []
persons.append(Person("Janek",23))
persons.append(Person('Grzesiek',23))
persons.append(Person('Agata',25))
for person in persons:
    person.introduce()

