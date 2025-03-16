class Stack: #definiowanie klasy stasy
    def __init__(self):    #definiowanie metody konstruktora
        self.__stack_list = []  #stosujemy enkapsulację __

    def push(self, item):
        self.__stack_list.append(item)

    def pop(self):
        item = self.__stack_list[-1]
        del self.__stack_list[-1]
        return item

stack1 = Stack()
stack2 = Stack()
stack3 = Stack()

for i in range(1,101):
        stack1.push(i)

for _ in range(100):
    stack2.push(stack1.pop())

for _ in range(100):
    stack3.push(stack2.pop())

for _ in range(100):
    print(stack3.pop(), end=" ")


