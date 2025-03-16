numbers = []
numbers_total = int(input("podaj liczbę elementów zbioru: "))
for i in range(numbers_total):
    number = int(input("Podaj " + str(i + 1) + " element zbioru: "))
    numbers.append(number)
print(numbers)
numbers.sort(reverse=True)
print(numbers)
final_numbers = []
for number in numbers:
    if number not in final_numbers:
        final_numbers.append(number)
print(final_numbers)
