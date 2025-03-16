class MyClass:
    y = 99
    def my_method(self,x):
        self.x = 78
        self.other_method()
        print("To jest moja metoda",x, self.y)

    def other_method(self):
        print("To jest inna metoda")
obj = MyClass()
obj.my_method(3)
print(obj.x)
obj.my_method(4)

