class MyClass:

    x =1
    def __init__(self,value =1):
        if value%2==0:
            self.a = value
        else:
            self.b = value

obj1 = MyClass(1)
obj2 = MyClass(2)

if hasattr(obj1,'a'):
    print(obj1.a)
if hasattr(obj1,'b'):
    print(obj1.b)

if hasattr(MyClass,'x'):
    print(MyClass.x)


