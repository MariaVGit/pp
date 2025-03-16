def introduce(first_name="Jan", last_name="Kowalski"):
    print("Cześć, jestem  " + first_name + " " + last_name)
introduce(last_name = "V", first_name = "M")
print("raz","dwa","trzy",sep="-")
introduce()

def show_name(name="Jan"):
    print("Cześć, mam na imię {}.".format(name))
    return None
show_name("M")
show_name()
print(show_name("Marcin"))

def empty_function():
    pass
print(empty_function())

if empty_function() is None: #is None, == None; is not None, != None
    print("Funkcja nic nie zwróciła!")
    