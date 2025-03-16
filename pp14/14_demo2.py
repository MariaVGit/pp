phones = {"Tom":554658698566,"Ada":4745678285596,"Karol":576858604852}
#ten sam klucz nie można wykorzystywać 2 razy
print(phones)
animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik":"hamster"
}
print(animals_dict["kot"])
print(animals_dict.get("kot"))

#print(animals_dict["wiewórka"]) - will not work
#print(animals_dict.get("wiewiórka") - will return the value None
print(animals_dict.get("wiewiórka", "Brak takiego klucza w słowniku"))
print(animals_dict.get("kot", "Brak takiego klucza w słowniku"))

words = ["kot","lew","chomik"]
for word in words:
    if word in animals_dict.keys():
        print(word, "->",animals_dict[word])
    else:
        print("Nie znaleziono słowa {}  w słowniku".format(word))

for key in animals_dict.keys():
    print(key,"->",animals_dict[key])

for value in animals_dict.values():
    print(value)
for item in animals_dict.items():
    print(item)
for key, value in animals_dict.items():
     print(key,"->",value)

animals_dict["świnka"] = "pig"
print(animals_dict)

animals_dict.popitem()
print(animals_dict)

animals_dict.clear()
print(animals_dict)







