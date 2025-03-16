a,b,c = 2,3,4
if a < b < c:
    print("!!!")

a = 5
b = 3
#koniukcja bitowa
print(a, "&", b, "=", a & b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a))

#alternatywa bitowa
print(a, "|", b, "=", a | b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a | b))

#alternatywa rozłączna bitowa
print(a, "^", b, "=", a ^ b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a ^ b))

print()
#przesunięcie bitowe w prawo
print(a, ">>", b, "=", a >> b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a >> b))


# negacja bitowa
print("~" + str(a), "=", ~a)
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(~a))

print(~1)
#00000001 (1) -> 11111110 (-2)
#00000000 (0)
#11111111 (-1)
#11111110 (-2)

#for i in range(5, -6, -1):
    #print("{0:08b} => {1:d}".format( *args: i &255, i)

#Xql'gf(bm{|(nibfq)
#rozszyfruj wiadomość
#szyfr:dla każdego znaku zmieniono 4 bit na przeciwny
#bity liczymy od najmniej znaczącego

print(ord("c"), chr(99))
print("{:08b}".format(ord("c")))
#01100011 -> chcemy zmienić 4 bit (od prawej)
#00001000 ->maska pozwala nam wyizolować dany bit
#01101011 ->używamy XORa (alternatywa rozłączna), do zmiany bitu

print("{:08b}".format(1 << 3))
print("{:08b}".format(ord("c") ^ (1 << 3) ))

print()
str = "Xql'gf(bm{|(nibfq)"
for c in str:
    n = ord(c) ^ (1 << 3)
    print(chr(n), end="")


