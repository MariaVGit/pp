#ciąg Fibonacciego
# 1 1 2 3 5 8
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    elem_1  = elem_2 = 1
    sum = 0
    for i in range(3, n+1):
        sum = elem_1 + elem_2
        elem_1,elem_2 = elem_2,sum
    return sum
for n in range(1,10):
    print(n, "->", fib(n))
print(fib(6))


