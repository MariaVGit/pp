def get_number(number_no):
    print("Proszę podaj {} liczbę:".format(number_no))
    return int(input())
a = get_number(1)

b = get_number(2)

c= get_number(3)
print("Pobrano liczby: ", a, b, c)

print("Podbrano liczby:",get_number(1), get_number(2), get_number(3))


