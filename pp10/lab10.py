number = int(input("Podaj liczbę elementów: "))

list = []
for i in range(number):
    i = input("Podaj " + str(i+1) + " imię: ")
    list.append(i)
print(list)
print("Imiona pobrane od użytkownika to: ", end=" ")
for i in range(len(list)):
    print(list[i],end=" ")



