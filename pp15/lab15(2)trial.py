counter = 0
while counter < 3:
    try:
        number = int(input("Wprowadź numer: "))
        counter += 1
    except:
        print("To nie jest liczba zmiennoprzecinkowa")
