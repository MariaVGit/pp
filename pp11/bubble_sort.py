numbers = [4,5,2,1]
numbers.sort(reverse=True)
print(numbers)
#swapped = True
#while swapped:  #doesn't work
    #swapped = False
    #for i in range(len(numbers)-1):
         #if numbers[i] > numbers[i+1]:
             #numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
         #swapped = True

print(numbers) #doesn't work

list_1 = [9]
list_2 = list_1 # kopiuje nazwę listy, a nie jej zawartość
list_2 = list_1[:] #kopiuje całą listę
list_2[0] =13
print(list_1)
#wycinki (slicing)
#lista[start:end]
#          -5 -4 -3-2-1
numbers = [10,8,6,4,2]
new_numbers = numbers[1:4]
print(new_numbers)
new_numbers = numbers[-4:4]
print(new_numbers)
new_numbers = numbers[4:3]
print(new_numbers)
new_numbers = numbers[3:]
print(new_numbers)
del numbers[-2:]
print(new_numbers)