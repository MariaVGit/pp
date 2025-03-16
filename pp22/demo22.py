class MyClass:
    counter = 0 # zmienna klasy
    def __init__(self,x=1):
        self.x = x
    def sety(self, y):
        self.y = y

obj = MyClass()
print(obj.x)
obj1 = MyClass(99)
print(obj1.x)

obj2 = MyClass(0)
obj2.sety(0)

obj3 = MyClass()
obj3.z = 1

print(obj.__dict__)

class MyClass:
    counter = 0
    def __init__(self,x=1):
        self.__x = x
        MyClass.counter += 1

obj4 = MyClass()
obj5 = MyClass(2)
obj6 = MyClass(3)

print(MyClass.counter)
print(obj5.counter)

print(obj4.__dict__, obj4.counter)
print(obj5.__dict__, obj5.counter)

print(MyClass.__dict__)
print(obj4.__dict__)
