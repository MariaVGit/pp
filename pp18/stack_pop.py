stack = []
stack2 = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push("Ala")
push("ma")
push("kota")

print(pop())
print(pop())
print(pop())
