number = int(input("Podaj liczbę: "))
if number ** (1/2) % 1 ==0:
    str1 = "Tak"
    str2 = ""
else:
    str1 = "Nie"
    str2 = "nie"
print(str1 + ", pierwiastek kwadratowy z liczby " + str(number) + " " +str2 + " jest liczbą całkowitą")



points = int(input("Wprowadź liczbę punktów(1-100): "))
print("Twoja ocena jest", end=" ")
if points >= 95:
    print("Ocena 5")
elif points > 84:
    print("Ocena 4,5")
elif points >= 70:
    print("Ocena 4")
elif points > 60:
    print("Ocena 3,5")
elif points > 50:
    print("Ocena 3")
else: print("Ocena 2")



import random
number = random.randint(1, 10)
msg = "Masz kolejną szansę, moja liczba jest "
guess = int(input("Zgadnij liczbę(1-10): "))
if guess == number:
    print("Brawo! Dokładnie taką liczbę miałem na myśli")
else:
    msg = "Masz kolejną szansę, moja liczba jest "
    if number % 2 == 0:
        msg += "parzysta: "
    else:msg += "nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Brawo, udało się za drugim razem")
    else:
        msg = "Masz ostatnią szansę, liczba jest "
        if number >5:
            msg += "większa niż "
        else:
            msg += "mniejsza lub równa "
        msg += "pięć: "
        guess = int(input(msg))
        if guess == number:
            print("Zgadłeś")
        else:
            print("Niestety, myślałem o liczbie " + str(number) + ".")



