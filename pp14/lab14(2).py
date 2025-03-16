def merge_lists(source,target):
    for element in source:
        if element not in target:
            target.append(element)

def transform_data(list1,list2,list3):
    result = []
    merge_lists(list1,result)
    merge_lists(list2,result)
    merge_lists(list3,result)
    return tuple(result)

print(transform_data([1,2,],[1,1],[4,4,4]))
print(transform_data([1,2,3],[1,2,3],[4,5,6]))
print(transform_data(["Ala","ma"],["Ala","ma","kota"],["mysz"]))





