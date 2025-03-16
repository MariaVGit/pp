class MyClass:
    def __init__(self):
        self.x = 1

obj1 = MyClass()
obj2 = MyClass()
obj3 = obj1

print(obj1 is obj2)
print(obj2 is obj3)
print(obj1 is obj3)

obj3.x = 99
print(obj1.x)
print(obj1.x,obj2.x,obj3.x)

str1 = "ala ma"
str2 = "ala ma kota"
str1 += " kota"
print(str1)
print(str2)
print(str1 == str2, str1 is str2)

