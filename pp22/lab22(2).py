class C:
    counter = 0
    def __init__(self):
        C.counter += 1

    def get_counter(self):
        return C.counter

for _ in range (100):
    c = C()

print(C.counter)
print(c.get_counter())

