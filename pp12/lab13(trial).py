list1 = [2,3,4,5]
def function1(list,n):
    for i in range(len(list)):
        list[i] = list[i] ** n

    return list
print(function1(list1,2))

