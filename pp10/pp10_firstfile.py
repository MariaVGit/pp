numbers = [3,2,11,2,20]
print(numbers)

fruits = ['apple','banana','cherry']
print(fruits)
print(fruits[-1],fruits[-3])
#pozwala przechowywać elementy o róźnych typach
numbers = [1,"jeden",True,2.0,9]
print(numbers)
#elementy listy są zawsze numerowane od zera
print(numbers[0], numbers[1])

fruits = ['apple','banana','cherry']
for i in range(len(fruits)):
    print(fruits[i])

for fruit in fruits:
    print(fruit)
