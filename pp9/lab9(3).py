number = int(input("Podaj liczbę: "))
n = int(input("Podaj nr bitu: "))
#sprawdzenie
mask = 1 << n
result = number & mask
print("{:08b}".format(number))
print("{:08b}".format(mask))
print("-" * 8)
print("{:08b}".format(result))
bit  = int(bool(result))
print("Bit na pozycji", n, "dla liczby", number, "wynosi", str(bit))
