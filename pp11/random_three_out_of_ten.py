#wylosuj 3 liczby ze zbioru od 1-10 bez powtórzeń, posortuj wynik
import random
random_numbers = []
counter = 3
while counter:

    number = random.randint(1, 10)
    if number not in random_numbers:
        random_numbers.append(number)
        counter -= 1
    random_numbers.sort()
print(random_numbers)

numbers = [i for i in range(1, 11)]
random_numbers = random.sample(numbers,3) #losowanie liczb we zbioru bez powtórzeń
random_numbers.sort()
print(random_numbers)
