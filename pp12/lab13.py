def pow(numbers,exponent):
    numbers = numbers[:] #zabiezpieczenie przed modyfikacją listy
    for i in range(len(numbers)):
        numbers[i] = numbers[i]**exponent
    return numbers

numbers = [1,2,3]
print(pow(numbers,2))

def pow2(numbers,exponent):
    result = []
    for n in numbers:
        result.append(n**exponent)
    return result
print(pow2(numbers,2))

def pow3(numbers,exponent):
    return[x**exponent for x in numbers]
print(pow3(numbers,2))






