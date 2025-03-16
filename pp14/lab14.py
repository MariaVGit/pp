phones = {"Aga":374675695456,"Marcin":378459564069,"Tomek":37485750685,"Iza":847595068590}
while True:
    name = input("Wprowadź imię: ")
    if name == "":
        break
    if name in phones:
        print("Telefon",phones[name])
    else:
        print("Nie znaleziono numeru telefonu")



