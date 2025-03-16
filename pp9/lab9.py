number1 = int(input("Liczba początkowa: "))
number2 = int(input("Liczba końcowa: "))
is_first = True
print("Liczby z zakresu od ", number1,"do ", number2, "podzielne przez 3 lub 5 lub 7 to: ", end=" ")
for i in range(number1, number2 +1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        if not is_first:
            print(", ", end="")
        print(i, end=" ")
    is_first = False
print(".")

