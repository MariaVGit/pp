import random
numbers = []
random_numbers = []
hit_total = 0
for i in range(6):
    numbers.append(int(input("Podaj liczbę " + str(i +1) + " (1-49): ")))
print(numbers)
random_numbers = random.sample(range(1,50),6)
print(random_numbers)
numbers.sort()
random_numbers.sort()
print(numbers)
print(random_numbers)
for number in numbers:
    if number in random_numbers:
        hit_total += 1
print("Trafiono ",hit_total, "liczb.")




