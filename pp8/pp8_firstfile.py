i = 0
while i < 10:
    print(i, end=" ")
    i += 1
for i in range(0, 10):
    print(i, end=" ")

for i in range(0, 10, 1):
    print(i)
for i in range(10):
    print(i)
for i in range(3, 10, 2):
    print(i)
for i in range(9, -1, -1):
    print(i)

#3! = 1*2*3 = 6
number = 5
factorial = 1

#for i in range(1, number + 1):
#   factorial *= i  #factorial = factorial * i

while number:
    factorial *= number
    number -= 1
print(factorial)

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Koniec pętli")


