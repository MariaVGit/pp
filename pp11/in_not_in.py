numbers = [1,2,3,4,5]
print(5 in numbers)
print(6 not in numbers)

#wyrażenia listowe

numbers = [i*2 for i in range(1,101)]
print(numbers)

numbers = [i for i in range(1,101) if i%2 == 0]
print(numbers)

#1-300 ile liczb podzielnych przez 3 i 7
print(len([i for i in range(1,301) if i %3 == 0 and i%7 == 0]))

print([[1,2],[3,4]])
row = [1,2]
matrix = [row[:],row[:]]
print(matrix)
matrix[0][0] = 99
print(matrix)

