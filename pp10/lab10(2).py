import random
lists = []
for i in range(16):
    lists.append(random.randint(1,6))
print(lists)
print(lists[7])
counter = 0
for list in lists:
    if list == 6:
        counter += 1
print(counter)




