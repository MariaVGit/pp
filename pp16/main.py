import modul_demo
print(dir(modul_demo))
help(modul_demo)
print("Czy to jest ciąg znaków?", modul_demo.is_string("test"))
print("Suma elementów listy:", modul_demo.sum_list_elem([3,4,5,2,83]))
print(modul_demo.__name__)
