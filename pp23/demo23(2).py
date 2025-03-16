class MyClass:
    def __init__(self,name):
        print("Inicjalizuje objekt")
        self.__name = name
    def get_name(self):
        return self.__name

obj =MyClass("Marcin") #tworzenie instancji klasy MyClass
print(obj.get_name())

