a = 1
b = 4

print("a=",a, "b=",b)
tmp = a
a = b
b = tmp

print("a=",a, "b=",b)

numbers = [1,2,3]

numbers[0], numbers[1] = numbers[1], numbers[0]
print(numbers)

#[4,5,2,1]
#[4,2,5,1]
#[2,4,1,5]
#[1,2,4,5]
