class Stack: #definiowanie klasy stasy
    def __init__(self):    #definiowanie metody konstruktora
        self.__stack_list = []  #stosujemy enkapsulację __

    def push(self, item):
        self.__stack_list.append(item)

    def pop(self):
        item = self.__stack_list[-1]
        del self.__stack_list[-1]
        return item

    def empty(self):
        return len(self.__stack_list) == 0

    def size(self):
        return len(self.__stack_list)

    def top(self):
        return self.__stack_list[-1]

stack = Stack()
print("Jest pusty?", stack.empty())

stack.push("Ala")
stack.push("Tomek")
print("Jest pusty?", stack.empty())
print("Ile elementów?", stack.size())
print("Na samej górze?", stack.top())

print(stack.pop())
print(stack.pop())


