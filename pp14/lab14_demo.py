numbers = (1,) # dodać przecinek żeby zaznaczyć że to krotka(tuple)
print(numbers)
numbers = (1, 2, 3)
print(numbers[-1])
for number in numbers:
    print(number)
print(numbers[1:])
numbers = tuple(x for x in range(10) if x%2 == 0)
numbers = (1,2,3)
#numbers[0]=999 - this will not work
print(len(numbers))
print(numbers+numbers)
numbers = [1,2,3]
print(numbers,type(numbers))
numbers = tuple(numbers)
print(numbers,type(numbers))
letters = tuple("Ala ma kota.")
print(letters)
letters = list(" ma kota.")
print(letters)

