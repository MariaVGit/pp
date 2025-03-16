class MyClass:
    def __my_private_method(self):
        print("I am a private method")

obj = MyClass()
print(MyClass.__dict__)
print(type(obj).__name__)

class A:
    pass

class B(A):
    pass

class C(A,B):
    pass

print(C.__bases__)


