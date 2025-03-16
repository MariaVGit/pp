#wylosuj 10 dowolnych liczb od 1 do 100
#umieść w liście
#wyświetl listę
import random
numbers = []
for i in range(10):
    number = random.randint(1, 100)
    numbers.append(number)
print(number)
