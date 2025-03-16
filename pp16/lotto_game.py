from lotto import get_user_numbers, draw_numbers, check_user_numbers

print("Witaj w grze lotto!")
user_numbers = get_user_numbers()
print("Pobrane liczby to: ", user_numbers)
print("\nNaciśnij ENTER aby dokonać losowania liczb!\n")
input()
lucky_numbers = draw_numbers()
print("Wylosowano liczby:", lucky_numbers)
print()

result = check_user_numbers(user_numbers,lucky_numbers)
if result == 6:
    print("Gratulacje!")
elif result == 5:
    print("Trafiłeś 5, brawo!")
elif result == 4:
    print("Hurra, trafiono 4")
elif result == 3:
    print("Trafiono 3")
elif result == 2 or result == 1:
    print("Trafiono {} liczę/y".format(result))
else:
    print("To nie jest twój dzień")


