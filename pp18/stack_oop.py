class Stack: #definiowanie klasy stasy
    def __init__(self):    #definiowanie metody konstruktora
        self.__stack_list = []  #stosujemy enkapsulację __

    def push(self, item):
        self.__stack_list.append(item)

    def pop(self):
        item = self.__stack_list[-1]
        del self.__stack_list[-1]
        return item

stack_obj = Stack()

stack_obj.push(3)
stack_obj.push(2)
stack_obj.push(1)

print(stack_obj.pop())
print(stack_obj.pop())
print(stack_obj.pop())

stack1 = Stack()
stack2 = Stack()

stack1.push(3)
stack1.push("Ala")

stack2.push(2)
stack2.push("ma")

print(stack1.pop())
print(stack2.pop())
print(stack1.pop())
print(stack2.pop())

class StackSum(Stack): #definiujemy nową klasę dziedziczącą po klasie Stack
    def getSum(self):
        return sum(self._Stack__stack_list)

stack = StackSum()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.getSum())
print(stack.pop())

for i in range(1000):
    stack.push(i)

print(stack.getSum())
for _ in range(1000):
    print(stack.pop(), end =",")


