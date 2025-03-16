class Car:
    def drive(self):
        print("Jedzie>>>")

class Boat:
    def sail(self):
        print("Płynie>>>")

class Amphibia(Car,Boat):
    pass

amphibia = Amphibia()
amphibia.drive()
amphibia.sail()

class Left:
    x = "L"
    x_left = "ll"

    def foo(self):
        return "left"
class Right:
    x = "r"
    x_right = "rr"
    def foo(self):
        return "right"

class Subclass(Left,Right):
    pass

obj = Subclass()
print(obj.foo())
print(obj.x_right)
