def sum_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

numbers = [1,2,3,4,5]
print(sum_numbers(numbers))

def scope_test():
    x = 123
    print(x)
scope_test()
#print(x)

def scope_test2():
    global x
    x = 999 #zmienna lokalna, nadpisała zmienną globalną
    print("w środku funkcji:",x)
x = 123
scope_test2()
print("poza funkcją",x)
