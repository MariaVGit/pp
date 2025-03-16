names = []
total_elements = int(input("Podaj liczbę imion: "))
for i in range(total_elements):
    names.append(input("Podaj " + str(i +1) + "imię: "))
print("Lista imion: ", names)
